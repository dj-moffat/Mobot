import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import RPi.GPIO as GPIO

class MowerBladeNode(Node):

    def __init__(self):
        super().__init__('mower_blade_node')
        '''
        self.pwm_pin = 18  # Set to the GPIO pin you are using
        self.frequency = 50  # Frequency in Hz
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.frequency)
        self.pwm.start(0)  # Start PWM with 0% duty cycle

        self.declare_parameter('duty_cycle', 0.0)
        #self.timer = self.create_timer(.5, self.timer_callback)
        '''
        self.subscription = self.create_subscription(Joy,'joy',self.joy_callback,10)
        self.subscription  # prevent unused variable warning

    def joy_callback(self, msg):
        self.get_logger().info(f'Received Joy message: {msg}')
        '''
        duty_cycle = self.get_parameter('duty_cycle').get_parameter_value().double_value
        self.pwm.ChangeDutyCycle(duty_cycle)
        self.get_logger().info(f'Set PWM duty cycle to {duty_cycle}%')
        '''

    def __del__(self):
        self.pwm.stop()
        GPIO.cleanup()



def main(args=None):
    rclpy.init(args=args)
    node = MowerBladeNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
