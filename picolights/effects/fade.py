from adafruit_led_animation.animation import Animation
from picolights.pixelwrapper import Color, PixelWrapper

def _fade(color: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(c - (c / 4) for c in color)

class DimmableColor(Color):

    def __init__(self, value):
        super().__init__(value)
        self._start_value = value
        self._brightness = 1.0

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, value):
        self._brightness = value
        self.value = tuple(int(c * value) for c in self._start_value)

    @property
    def total(self):
        return sum(self.value)
    
    def __add__(self, other):
        return self.total + other
    
def smooth(value, factor=256/6):
    return round(factor * (value // factor))
    
def smooth_rgb(value: tuple):
    return tuple(smooth(v) for v in value)


class Fade(Animation):

    on_cycle_complete_supported = True

    def __init__(self, pixel_object, *args, **kwargs):
        super(Fade, self).__init__(PixelWrapper(pixel_object), *args, **kwargs)
        self._start_values = None

    def draw(self):
        if not self._start_values:
            self._start_values = tuple(smooth_rgb(p) for p in self.pixel_object)
            self._reduced_colors = {c: DimmableColor(c) for c in set(self._start_values)}
            self.values = tuple(self._reduced_colors[c] for c in self._start_values)

        total = sum(c.total for c in self._reduced_colors.values())
        if total > 0:
            for c in self._reduced_colors.values():
                c.brightness = c.brightness - 0.01
            self.pixel_object[:] = self.values
        else:
            self.cycle_complete = True
            self._start_values = None

        


