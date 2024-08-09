import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import gpiod

class BladeListenerNode(Node):

    def __init__(self):
        super().__init__('blade_listener_node')

        self.subscription = self.create_subscription(Joy,'joy',self.joy_callback,10)
        self.subscription  # prevent unused variable warning

    def joy_callback(self, msg):
        self.get_logger().info(f'X button status: {msg.buttons[0]}')
        

        

def main(args=None):
    rclpy.init(args=args)
    node = BladeListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
