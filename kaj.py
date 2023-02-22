import board
import neopixel
import time
import adafruit_led_animation.color as color

from picolights.colors import random_color
from picolights.effects import Blend, Chase, Rainbow

from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.sequence import AnimationSequence

pixel_pin=board.GP21
num_pixels=300

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

blend = Blend(pixels, 0, random_color())
blend.add_cycle_complete_receiver(lambda a: setattr(a, 'color', random_color()))

comet = Comet(pixels, speed=0, color=random_color(), tail_length=10, bounce=True)
comet.add_cycle_complete_receiver(lambda a: setattr(a, 'color', random_color()))

chase = Chase(pixels, speed=0, color=random_color())
chase.add_cycle_complete_receiver(lambda a: setattr(a, 'color', random_color()))

rainbow = Rainbow(pixels, speed=0, color=random_color(), scale=2)

animations = AnimationSequence(blend, rainbow, advance_on_cycle_complete=True)

while True:
    animations.animate()