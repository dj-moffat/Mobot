import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from gpiozero import PWMOutputDevice, DigitalOutputDevice
from collections import deque

class WheelListenerNode(Node):
    def __init__(self, name, pwm_pin, dir_pin, joy_axis, is_left):
        super().__init__(name)
        
        # PWM setup using gpiozero
        self.pwm = PWMOutputDevice(pwm_pin)
        
        # Direction pin setup using gpiozero
        self.dir = DigitalOutputDevice(dir_pin)
        
        self.speed = 0
        self.joy_axis = joy_axis
        self.is_left = is_left
        
        self.speed_history = deque(maxlen=5)  # For input smoothing
        
        self.subscription = self.create_subscription(Joy,'joy',self.joy_callback, 10)

    def joy_callback(self, msg):
        if len(msg.axes) > self.joy_axis:
            new_speed = msg.axes[self.joy_axis] * 0.5  # Reduce speed by 50%
            self.speed_history.append(new_speed)
            self.speed = sum(self.speed_history) / len(self.speed_history)  # Average for smoothing
            self.update_motor()
            self.get_logger().info(f"{self.get_name()} speed: {self.speed:.2f}")

    def update_motor(self):
        dead_zone = 0.1
        if abs(self.speed) < dead_zone:
            self.pwm.value = 0
            self.dir.value = 0
        else:
            # Smooth transition from dead zone
            adjusted_speed = (abs(self.speed) - dead_zone) / (1 - dead_zone)
            adjusted_speed = max(0, min(adjusted_speed, 1))  # Clamp between 0 and 1
        
            # Set direction based on is_left
            if self.is_left:
                direction = 1 if self.speed > 0 else 0
            else:
                direction = 0 if self.speed > 0 else 1
        
            self.dir.value = direction
        
            # Set PWM duty cycle
            self.pwm.value = adjusted_speed

def main(args=None):
    rclpy.init(args=args)
    left_wheel = WheelListenerNode('left_wheel', 13, 6, 0, True)
    right_wheel = WheelListenerNode('right_wheel', 12, 16, 1, False)
    
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(left_wheel)
    executor.add_node(right_wheel)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        for wheel in [left_wheel, right_wheel]:
            wheel.pwm.value = 0
            wheel.dir.value = 0
            wheel.pwm.close()
            wheel.dir.close()
        executor.shutdown()
        rclpy.shutdown()

if __name__ == '__main__':
    main()