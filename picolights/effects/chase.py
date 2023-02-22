import time
from rainbowio import colorwheel


def color_chase(controller, color, wait: int = 0):
    pixels = controller.pixels
    num_pixels = controller.num_pixels

    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
