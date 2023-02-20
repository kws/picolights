import time
from rainbowio import colorwheel

from ..controller import Controller

_quart = 256 // 6

def blend(controller: Controller, color, wait=0):
    pixels = controller.pixels
    num_pixels = controller.num_pixels

    color = color + 256

    start_col = colorwheel(color - _quart)
    end_col = colorwheel(color + _quart)
    color = colorwheel(color)

    print("start", start_col)
    print("end", end_col)

    for i in range(num_pixels):
        if i < num_pixels // 2:
            pixels[i] = start_col
            pixels[num_pixels-i-1] = end_col
        else:
            pixels[i] = color
            pixels[num_pixels-i-1] = color

        pixels.show()