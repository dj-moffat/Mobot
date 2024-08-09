# if you don't need to be wireless, check out the library pydualsense

#import time
from evdev import InputDevice, categorize, ecodes                   # pip install evdev
gamepad = InputDevice('/dev/input/event5')      # "cd /dev/input" then "ls -al" to see your connections

button_presses = {                          # ecodes.EV_KEY
    304: 'X',
    305: 'circle',
    306: 'abc',
    307: 'triangle',
    308: 'square',
    309: 'R1',
    310: 'L1',      
    311: 'R1',
    312: 'L2',
    313: 'R2',
    314: 'share',
    315: 'pause',
    316: 'playstation',
    317: 'touchpad'
}

button_values = {                           # ecodes.EV_KEY button press values
    0: 'up',
    1: 'down'
}

absolutes = {                               # ecodes.EV_ABS
    #0: 'left joystick left/right',          # 0 = left, 255 = right
    1: 'left joystick up/down',             # 0 = up, 255 = down
    #2: 'right joystick left/right',         # 0 = left, 255 = right
    #3: 'L2 analog',                         # 0 = no press, 255 = full press
    4: 'right joystick up/down',                         # 0 = no press, 255 = full press
    #5: 'Unknown A',            # 0 = up, 255 = down
    16: 'leftpad left/right',               # -1 = left, 0 = stop pressing, 1 = right
    17: 'leftpad up/down',                  # -1 = up, 0 = stop pressing, 1 = down
}

leftpad_left_right_values = {
    -1: 'left',
    0: 'left-right stop',                   # stoip means that the button was no longer pressed
    1: 'right'
}

leftpad_up_down_values = {
    -1: 'up',
    0: 'up-down stop',
    1: 'down'
}

CENTER = 128
BLIND = 6                                   # there's a lot of drift at 128, so don't report changes within (128 - this value)
MAX_EMERGENCY_DELAY = 1000                  # max number of milliseconds between taps to qualify as an emergency double-tap

#emergency_tap_time = 0                      # track when the last time the emergency button (touchpad) was pressed
left_joystick, right_joystick = [CENTER, CENTER], [CENTER, CENTER]


#def is_emergency(event):
#    global emergency_tap_time
#    if event.code == 317 and direction == 'down':                           # emergency tap-down on the touchpad
#        previous_tap = emergency_tap_time
#        emergency_tap_time = int(round(time.time() * 1000))                 # set now as the most recent tap time
#        if emergency_tap_time < (previous_tap + MAX_EMERGENCY_DELAY):       # if the current tap-down comes less than x milliseconds after last tap
#            return True
#    return False

#def update_left_joystick_position(event):
#    global left_joystick
#    if event.code == 0:                     # left joystick, y-axis (left/right)
#        left_joystick[0] = value
#    elif event.code == 1:                   # left joystick, x-axis (up/down)
#        left_joystick[1] = value

#def update_right_joystick_position(event):
#    global right_joystick
#    if event.code == 2:                     # right joystick, y-axis (left/right)
#        right_joystick[0] = value
#    elif event.code == 5:                   # right joystick, x-axis (up/down)
#        right_joystick[1] = value

#def decode_leftpad(event):
#    action  = ''
#    if event.code == 16:                    # leftpad, either a left or right action
#        action = leftpad_left_right_values[value]
#    elif event.code == 17:                  # leftpad, either an up or down action
#        action = leftpad_up_down_values[value]
#    else:                                   # unhandled event
#        return ''
#    return f'leftpad: {action}'


if __name__ == '__main__':
    # print(gamepad)

    for event in gamepad.read_loop():

        if event.type == ecodes.EV_KEY and event.code in button_presses:       # any button press other than leftpad
            tmp=''
            button, direction = button_presses[event.code], button_values[event.value]
            print(f'{button} {direction}')

            #if is_emergency(event):
                #print('EMERGENCY BUTTON!')

        if event.type == ecodes.EV_ABS and event.code in absolutes:                     # leftpad, joystick motion, or L2/R2 triggers
            action, value = absolutes[event.code], event.value

            #if event.code in [2, 5]: #0,1                                              # joystick motion
                #if event.code in [0, 1]:                                                # left joystick moving
                    #update_left_joystick_position(event)
                #elif event.code in [2, 5]:                                              # right joystick moving
                    #update_right_joystick_position(event)

                #if event.value > (CENTER - BLIND) and event.value < (CENTER + BLIND):   # skip printing the jittery center for the joysticks
                    #continue

                #print(f'{left_joystick}, {right_joystick}')
                #continue

            if event.code in [1,4]: # 3                                                    # L2/R2 triggers
               print("TEST")
               # print(f'{action} {value}')
            elif event.code in [16, 17]:                                                # leftpad (d-pad) action
                action = decode_leftpad(event)
                print(action)
