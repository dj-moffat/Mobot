import gpiod
import time
import os
from datetime import datetime, timedelta

# Current time
now = datetime.now()
print("Current time:", now)

# Add 5 days to the current time
future_time = now + timedelta(days=5)
print("Future time (5 days later):", future_time)

# Subtract 3 hours from the current time
past_time = now - timedelta(hours=3)
print("Past time (3 hours earlier):", past_time)

# Define the chip and line number (GPIO pin number)
chip = gpiod.chip('gpiochip4')  # Change if your chip is different
line = chip.get_line(2)  # Use the GPIO pin number connected to the button

# Request the line as an input
config = gpiod.line_request()
config.consumer = "shutdown_button"
config.request_type = gpiod.line_request.EVENT_RISING_EDGE
line.request(config)

print("Waiting for button press...")

try:
    while True:
        event = line.event_wait(timedelta(seconds=5))  # Wait for the button press event
        if event:
            print("Button pressed! Shutting down...")
            os.system("sudo /sbin/shutdown -h now")

            break

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    line.release()
