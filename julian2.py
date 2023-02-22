import board
import neopixel
import random
import time
from rainbowio import colorwheel

numpixels=145+50

pixels = neopixel.NeoPixel(board.GP21, numpixels, brightness=1, auto_write=False)
pixels.fill(0) 
b=5
c=10
def strip(i,b,c):   
    pixels[i-b] = color
    pixels[i-c] = 0
    time.sleep(0.001)
    
while True:
    a=random.randint(0,255)
    color = colorwheel(a)
    
    for i in range(0,numpixels):
        
        pixels[i] = (255,255,0)
        if i > 0:
            pixels[i-1] = 0
        time.sleep(0.001)
        strip(i,b,c)
        strip(i-10,b,c)
        strip(i-20,b,c)
        strip(i-30,b,c)
        strip(i-40,b,c)
        pixels.show()
                
    for i in range(0,numpixels):
        pixels[numpixels-1-i] = color
        pixels.show()
    
     

