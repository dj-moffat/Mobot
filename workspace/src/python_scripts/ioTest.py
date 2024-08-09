from gpiozero import PWMOutputDevice
import time

pwm = PWMOutputDevice(19)  # Use a hardware PWM pin

for i in [.1,.2,.3,.4]:
    pwm.value = i  # 50% duty cycle
    time.sleep(2)


'''
import gpiod
import time
import threading

# pins
POWER = 18

chip = gpiod.chip('gpiochip4')
power = chip.get_line(POWER)

power_config = gpiod.line_request()
power_config.consumer = "motor_movement"
power_config.request_type = gpiod.line_request.DIRECTION_OUTPUT

power.request(power_config)

# PWM settings
PWM_FREQUENCY = 1000  # Increased to 1000 Hz
duty_cycle = 0  # Initial duty cycle (0-100)

# PWM function with more precise timing
def pwm_control():
    period = 1.0 / PWM_FREQUENCY
    cycle_start = time.perf_counter()
    while True:
        on_time = period * (duty_cycle / 100.0)
        off_time = period - on_time
        
        if on_time > 0:
            power.set_value(1)
            while time.perf_counter() - cycle_start < on_time:
                pass
        
        if off_time > 0:
            power.set_value(0)
            while time.perf_counter() - cycle_start < period:
                pass
        
        cycle_start = time.perf_counter()

# Start PWM in a separate thread
pwm_thread = threading.Thread(target=pwm_control, daemon=True)
pwm_thread.start()

def run():
    global duty_cycle
    try:
        duty_cycle = 100  # Set to desired speed
        while True:
            time.sleep(0.1)  # Small delay to prevent CPU hogging
    finally:
        cleanup()

def cleanup():
    global duty_cycle
    duty_cycle = 0  # Gradually stop the motor
    time.sleep(0.5)  # Wait for the motor to stop
    power.set_value(0)
    power.release()

if __name__ == "__main__":
    run()


'''

'''
import gpiod
import time
import threading

# pins
POWER = 18

chip = gpiod.chip('gpiochip4')
power = chip.get_line(POWER)

power_config = gpiod.line_request()
power_config.consumer = "motor_movement"
power_config.request_type = gpiod.line_request.DIRECTION_OUTPUT

power.request(power_config)

# PWM settings
PWM_FREQUENCY = 100  # Hz
duty_cycle = 0  # Initial duty cycle (0-100)

# PWM function
def pwm_control():
    period = 1.0 / PWM_FREQUENCY
    while True:
        on_time = period * (duty_cycle / 100.0)
        off_time = period - on_time
        
        if on_time > 0:
            power.set_value(1)
            time.sleep(on_time)
        
        if off_time > 0:
            power.set_value(0)
            time.sleep(off_time)

# Start PWM in a separate thread
pwm_thread = threading.Thread(target=pwm_control, daemon=True)
pwm_thread.start()

def run():
    global duty_cycle
    try:
        while True:
            duty_cycle = 70
            """
            # Gradually increase brightness/speed
            for i in range(0, 101, 5):
                duty_cycle = i
                print(f"Duty Cycle: {duty_cycle}%")
                time.sleep(0.1)
            
            # Gradually decrease brightness/speed
            for i in range(100, -1, -5):
                duty_cycle = i
                print(f"Duty Cycle: {duty_cycle}%")
                time.sleep(0.1)
            """
    finally:
        cleanup()

def cleanup():
    power.set_value(0)
    power.release()

if __name__ == "__main__":
    run()
'''