from evdev import InputDevice, categorize, ecodes  # pip install evdev


gamepad = InputDevice('/dev/input/event5')      # "cd /dev/input" then "ls -al" to see your connections
button_presses = {304: 'X', 305: 'circle', 306: 'abc', 307: 'triangle', 308: 'square', 309: 'R1', 310: 'L1', 311: 'R1', 312: 'L2', 313: 'R2', 314: 'share', 315: 'pause', 316: 'playstation',317: 'touchpad'}  # ecodes.EV_KEY
button_values = {0: 'up', 1: 'down'}  # ecodes.EV_KEY button press values
absolutes = {1: 'left joystick up/down', 4: 'right joystick up/down', 16: 'leftpad left/right', 17: 'leftpad up/down'}
leftpad_left_right_values = {-1: 'left', 0: 'left-right stop', 1: 'right'}
leftpad_up_down_values = {-1: 'up', 0: 'up-down stop', 1: 'down'}


def decode_leftpad(event):
    action  = ''
    if event.code == 16:                    # leftpad, either a left or right action
        action = leftpad_left_right_values[value]
    elif event.code == 17:                  # leftpad, either an up or down action
        action = leftpad_up_down_values[value]
    else:                                   # unhandled event
        return ''
    return f'leftpad: {action}'


if __name__ == '__main__':

    for event in gamepad.read_loop():

        if event.type == ecodes.EV_KEY and event.code in button_presses:       # any button press other than leftpad
            button, direction = button_presses[event.code], button_values[event.value]
            print(f'{button} {direction}')

        if event.type == ecodes.EV_ABS and event.code in absolutes:   
            action, value = absolutes[event.code], event.value

            if event.code in [1,4]: # UP and DOWN on LEFT & RIGHT Joysticks               
                print(f'{action} {value}')
            elif event.code in [16, 17]:                                        
                action = decode_leftpad(event)
                print(action)

