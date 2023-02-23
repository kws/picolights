import board
import neopixel
import adafruit_pixelbuf
from picolights import colors
from picolights.pixelwrapper import PixelWrapper, Color

pixel_pin=board.GP21
num_pixels=300


pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
pixels = PixelWrapper(pixels)


pixels.fill(colors.random_color())
pixels.show()

pixels[0] = Color((255, 0, 0))

c = Color((0, 255, 0))
my_list = [c, c, c, c, c]
pixels[1:6] = my_list

c.value  = (0, 0, 255)
pixels[1:5] = my_list[:4]

pixels.show()
print(len(pixels))

def smooth(value, factor=256/6):
    return round(factor * (value // factor))

print(smooth(256), smooth(0))