import board
import neopixel
from adafruit_led_animation.animation.sparklepulse import SparklePulse
import adafruit_led_animation.color as color


pixel_pin=board.GP21
num_pixels=300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
blink = SparklePulse(pixels, 0, color.BLUE)

while True:
    blink.animate()