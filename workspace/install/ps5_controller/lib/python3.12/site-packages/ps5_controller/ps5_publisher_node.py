import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from evdev import InputDevice, categorize, ecodes  # pip install evdev
import time

button_presses = {304: 'X', 305: 'circle', 306: 'abc', 307: 'triangle', 308: 'square', 309: 'R1', 310: 'L1', 311: 'R1', 312: 'L2', 313: 'R2', 314: 'share', 315: 'pause', 316: 'playstation',317: 'touchpad'}
button_values = {0: 0, 1: 1}  # ecodes.EV_KEY button press values
absolutes = {1: 'left joystick', 4: 'right joystick', 16: 'dpad horizontal', 17: 'dpad vertical'}
leftpad_left_right_values = {-1: 'left', 0: 'left-right stop', 1: 'right'}
leftpad_up_down_values = {-1: 'up', 0: 'up-down stop', 1: 'down'}

buttons = {'X':0,'square':0,'triangle':0,'circle':0}
axes = {'left joystick': 0, 'right joystick': 0}

class PS5PublisherNode(Node):

    def __init__(self):
        super().__init__('ps5_publisher_node')
        self.publisher = self.create_publisher(Joy, 'joy', 10)  # Publisher for 'joy' topic
        self.create_timer(0.1, self.handle_button_press)

    def convert_value(self,x):
        # Ensure x is within the expected range
        if x < 0:
            x = 0
        elif x > 255:
            x = 255

        # Apply the linear transformation
        y = 1 - (2 / 255) * x
        y = round(y*100)
        y = y/100
        if y < .05 and y > -.05:
            return 0
        else:
            return y

    def handle_button_press(self):
        prev_l = axes['left joystick']
        prev_r = axes['right joystick']

        try:
            print("Attempting to connect controller")
            gamepad = InputDevice('/dev/input/event5')      # "cd /dev/input" then "ls -al" to see your connections
            print("Controller connected!")
        except:
            print("No controller found! Will attempt again in 10 seconds.")
            time.sleep(10)
            self.handle_button_press()

        for event in gamepad.read_loop():
            publish_event = False
            if event.type == ecodes.EV_KEY and event.code in button_presses:       # any button press other than leftpad
                button, button_state = button_presses[event.code], button_values[event.value]
                if button in buttons:
                    publish_event = True
                    buttons[button] = button_state

            if event.type == ecodes.EV_ABS and event.code in absolutes:
                axis, value = absolutes[event.code], event.value
                if event.code in [1,4]: # UP and DOWN on LEFT & RIGHT Joysticks
                    if axis in axes:
                        new_value = self.convert_value(value)
                        axes[axis] = new_value
                        if axis=='left joystick' and prev_l != axes[axis]:
                            publish_event = True
                        elif axis=='right joystick' and prev_r != axes[axis]:
                            publish_event = True
            
            if publish_event:
                self.publish_button_press(axes, buttons)


    def publish_button_press(self,axes, buttons):
        message = Joy()
        message.buttons = [buttons['X'],buttons['square'],buttons['triangle'],buttons['circle']]
        message.axes = [axes['left joystick'],axes['right joystick']]
        self.publisher.publish(message)
        self.get_logger().info("Message sent - Buttons: " + str(message.buttons) + " - Axes: " + str(message.axes))


def main(args=None):
    rclpy.init(args=args)
    node = PS5PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

