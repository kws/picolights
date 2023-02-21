import board
import neopixel
from adafruit_led_animation.animation.chase import Chase
import adafruit_led_animation.color as color

from picolights.effects.blend import Blend

pixel_pin=board.GP21
num_pixels=300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
blink = Blend(pixels, 0, color.PURPLE)

while True:
    blink.animate()