import time
from rainbowio import colorwheel

from ..controller import Controller

def rainbow_cycle(controller: Controller, wait=0):
    pixels = controller.pixels
    num_pixels = controller.num_pixels

    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

