import board
import neopixel
import random
import time
from rainbowio import colorwheel
numpixels=138
pixels = neopixel.NeoPixel(board.GP21, numpixels, brightness=0.6, auto_write=True)

# pixels[:3] = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] 
def rainbow():
    
    for g in range(1,5):
        a = random.randint(0,255)

        for i in range(0,numpixels):
            
            color = colorwheel(a)
            pixels[i] = color
            time.sleep(0.01)
            a=a+1
        for i in range(0,numpixels):
            pixels[i] = 0
            time.sleep(0.01)
            
        for i in range(0,numpixels):
            color = colorwheel(a)
            pixels[numpixels-1-i] = color
            time.sleep(0.01)
            a=a+1

        for i in range(0,numpixels):
            pixels[numpixels-1-i] = 0
            time.sleep(0.01)
def dash():
    for l in range(1,10):
        j = random.randint(0,255)
        for l in range(0,numpixels):
            color = colorwheel(j)
            pixels[l] = color
            j=j+1
        
        for l in range(0,numpixels):
            color = colorwheel(j)
            pixels[numpixels-1-l] = color
            j=j+1
def demon():
    for i in range(1,20):
        for p in range(40,80):
            k=random.randint(0,numpixels)
            color = colorwheel(k)
            pixels[p] = color
        pixels[0:40] = [255, 0, 0] * 40
        pixels[81:numpixels] = [(255,0,0)] * 64

def full_rambo():
    for i in range(1,20):
        start_color = random.randint(0, 256)
        step_size = 256 / numpixels

        my_pixels = [0] * numpixels
        for p in range(0, numpixels):
            my_pixels[p] =  colorwheel(start_color + (p * step_size)) 
        pixels[0:numpixels] = my_pixels
        time.sleep(0.1)
    pixels.fill(0)
def police():
    n=int(numpixels/2)
    for x in range(1,10):
        for s in range(1,100):
            pixels[0:n] = [0,0,s] * n
        for s in range(1,100):
            pixels[0:n] = [0,0,100-s] * n
        for q in range(1,100):
            pixels[n:numpixels] = [(q,0,0)] * n
        for q in range(1,100):
            pixels[n:numpixels] = [(100-q,0,0)] * n
def sweep():
    pixels.fill(0)
    for color in range(0,numpixels):
        i=int(color*1.8)
        pixels[color] = (i,0,255-i) 
        time.sleep(0.01)
def switch():
    pixels.fill(0)
    for p in range(1,10):
        b=numpixels/2
        for i in range(1,b):
            pixels[i]=(0,0,i*2)
        for i in range(1,b):
            x=int(b+i)
            pixels[x]=(255-i*4.6,0,0)
        for i in range(1,b):
            x=int(numpixels-i)
            pixels[x]=(0,0,i*2)
        for i in range(1,b):
            x=int(b-i)
            pixels[x]=(255-i*2,0,0)

def super():
    pixels.fill(100)
    a=random.randint(0,numpixels-3)
    for i in range(1,255):
        pixels[a:a+3] = ((255-i,255-i,255))*3
    time.sleep(1)

while True:
    #police()
    #rainbow()
    #dash()
    #demon()
    #time.sleep(1)
    #full_rambo()
    #sweep()
    #switch()
    super()