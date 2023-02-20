import time
import board
from picolights.controller import Controller

import alarm
import board
import time
import digitalio

import random

from picolights.effects import color_chase, rainbow_cycle, blend


print("Waking up")

controller = Controller(pixel_pin=board.GP21, num_pixels=300, brightness=0.3, auto_write=False)

blend(controller, random.randint(0, 256))

# Set an alarm for 60 seconds from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)

print("Sleeping")
# Deep sleep until the alarm goes off. Then restart the program.
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
