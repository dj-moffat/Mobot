import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from gpiozero import PWMOutputDevice

class BladeListenerNode(Node):
    def __init__(self):
        super().__init__('blade_listener_node')
        
        # GPIO setup using gpiozero
        # Note: For Raspberry Pi 5, hardware PWM is available on GPIO 12, 13, 18, 19
        # We're using GPIO 18 as in your original code
        self.motor = PWMOutputDevice(18, frequency=100)  # 100 Hz PWM frequency
        
        # Motor state
        self.motor_on = False
        self.duty_cycle = 0.35  # 35% speed
        
        # Create a subscription to the joy topic
        self.subscription = self.create_subscription(Joy, 'joy', self.joy_callback, 10)

    def joy_callback(self, msg):
        if msg.buttons and msg.buttons[0] == 1:
            self.motor_on = not self.motor_on
            if self.motor_on:
                self.motor.value = self.duty_cycle
                self.get_logger().info(f"Motor ON at {self.duty_cycle*100}% speed")
            else:
                self.motor.value = 0
                self.get_logger().info("Motor OFF")

def main(args=None):
    rclpy.init(args=args)
    node = BladeListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.motor.value = 0
        node.motor.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()



'''   
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import gpiod
import time

class BladeListenerNode(Node):
    def __init__(self):
        super().__init__('blade_listener_node')
        
        # GPIO setup
        self.chip = gpiod.chip('gpiochip4')
        self.power = self.chip.get_line(18)
        power_config = gpiod.line_request()
        power_config.consumer = "motor_movement"
        power_config.request_type = gpiod.line_request.DIRECTION_OUTPUT
        self.power.request(power_config)
        
        # Motor state
        self.motor_on = False
        self.duty_cycle = 15  # Set your desired duty cycle here
        
        # Create a subscription to the joy topic
        self.subscription = self.create_subscription(Joy,'joy',self.joy_callback,10)
        
        # Create a timer for PWM control
        self.pwm_timer = self.create_timer(0.01, self.pwm_callback)  # 100 Hz PWM frequency

    def joy_callback(self, msg):
        if msg.buttons and msg.buttons[0] == 1:
            self.motor_on = not self.motor_on
            self.get_logger().info(f"Motor {'ON' if self.motor_on else 'OFF'}")

    def pwm_callback(self):
        if self.motor_on:
            on_time = 0.01 * (self.duty_cycle / 100.0)
            self.power.set_value(1)
            self.get_logger().debug(f"PWM High for {on_time:.6f} seconds")
            time.sleep(on_time)
            self.power.set_value(0)
            self.get_logger().debug("PWM Low")
        else:
            self.power.set_value(0)

def main(args=None):
    rclpy.init(args=args)
    node = BladeListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.power.set_value(0)
        node.power.release()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

'''