import board
import neopixel
import adafruit_led_animation.color as color

from picolights.colors import random_color
from picolights.effects import Blend, Chase, Fade, Rainbow

from adafruit_led_animation.sequence import AnimationSequence

pixel_pin=board.GP21
num_pixels=300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

blend = Blend(pixels, 0, random_color())
blend.add_cycle_complete_receiver(lambda a: setattr(a, 'color', random_color()))

fade = Fade(pixels, speed=0, color=0)
rainbow_fade = Fade(pixels, speed=0, color=0)

chase = Chase(pixels, speed=0, color=random_color())
chase.add_cycle_complete_receiver(lambda a: setattr(a, 'color', random_color()))

rainbow = Rainbow(pixels, speed=0, color=random_color(), scale=2, notify_cycles=1)

animations = AnimationSequence(blend, fade, rainbow, rainbow_fade, advance_on_cycle_complete=True, auto_clear=False)

while True:
    animations.animate()
