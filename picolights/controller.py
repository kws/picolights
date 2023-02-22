import neopixel


class Controller:

    def __init__(self, pixel_pin, num_pixels, **kwargs):
        self.__pixels = neopixel.NeoPixel(pixel_pin, num_pixels, **kwargs)
        self.__num_pixels = num_pixels

    @property
    def pixels(self):
        return self.__pixels
    
    @property
    def num_pixels(self):
        return self.__num_pixels
    
