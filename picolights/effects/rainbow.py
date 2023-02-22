from rainbowio import colorwheel
from adafruit_led_animation.animation import Animation
from picolights.hsv import hsv_to_rgb, rgb_to_hsv

class Rainbow(Animation):

    on_cycle_complete_supported = True

    def __init__(self, *args, scale=1, **kwargs):
        super().__init__(*args, **kwargs)
        num_pixels = len(self.pixel_object)

        h, s, v = rgb_to_hsv(*self.color)

        scale = 360 * scale

        self._colors = [hsv_to_rgb(h + (i * scale // num_pixels), s, v) for i in range(num_pixels)]


    
    def draw(self):
        pixel_len = len(self.pixel_object)
        cur_pix = (self.draw_count - 1) % pixel_len

        self.pixel_object[:] = self._colors[cur_pix:] + self._colors[:cur_pix]

        if self.draw_count % len(self.pixel_object) == 0:
            self.cycle_complete = True


