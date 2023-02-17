# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
from picolights.controller import Controller
from picolights.effects import color_chase, rainbow_cycle
from picolights.colors import RED, GREEN, BLUE


controller = Controller(pixel_pin=board.GP21, num_pixels=300, brightness=0.3, auto_write=False)

pixels = controller.pixels


while True:
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    color_chase(controller, RED)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0)
    color_chase(controller, GREEN)
    # color_chase(CYAN, 0)
    color_chase(controller, BLUE)
    # color_chase(PURPLE, 0)

    for _ in range(5):
        rainbow_cycle(controller)  # Increase the number to slow down the rainbow
