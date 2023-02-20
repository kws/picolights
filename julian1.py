import board
import neopixel
import random
import time
from rainbowio import colorwheel

pixels = neopixel.NeoPixel(board.GP21, 300, brightness=0.3, auto_write=True)

# pixels[:3] = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] 
while True:
    a = random.randint(0,255)

    for i in range(0,300):
        
        color = colorwheel(a)
        pixels[i] = color
        a=a+1
    for i in range(0,300):
        pixels[299-i] = 0

        