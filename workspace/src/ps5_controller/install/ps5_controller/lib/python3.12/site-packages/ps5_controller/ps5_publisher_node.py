#! /home/mobot/ROS2/bin python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from dualsense_controller import DualSenseController

class PS5PublisherNode(Node):

    def __init__(self):
        super().__init__('ps5_controller_node')
        self.joy_pub = self.create_publisher(Joy, 'joy', 10)  # Publisher for 'joy' topic
        self.button_states = [False] * 12  # Initialize button states for 12 buttons (adjust as needed)

        device_infos = DualSenseController.enumerate_devices()
        if len(device_infos) >= 1:
            print("Found devices")
        else:
            print('No DualSense Controller available.')
            
        # Schedule timer to publish button states
        #self.create_timer(0.1, self.publish_button_states)

    def publish_button_states(self):
        if self.ps5_controller:
            # Read button states from PS5 controller using sixaxis
            buttons = self.ps5_controller.get_controllers()[0]['buttons']
            self.button_states = [button for button in buttons]  # Update button states

        msg = Joy()
        msg.buttons = self.button_states
        self.joy_pub.publish(msg)


def main():
    rclpy.init_application()
    node = PS5PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
