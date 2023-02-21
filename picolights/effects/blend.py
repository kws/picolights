import random
from picolights.hsv import hsv_to_rgb, rgb_to_hsv
from adafruit_led_animation.animation import Animation

from ..controller import Controller

_fraq = 360 / 6


class Blend(Animation):

    on_cycle_complete_supported = True


    def _set_color(self, color):
        h, s, v = rgb_to_hsv(*color)

        self._start_col = hsv_to_rgb(h - _fraq, s, v)
        self._end_col = hsv_to_rgb(h + _fraq, s, v)
        super()._set_color(color)


    def draw(self):
        cur_pix = (self.draw_count - 1) % len(self.pixel_object)
        pixel_len = len(self.pixel_object)

        if cur_pix >= pixel_len / 2:
            self.pixel_object[cur_pix] = self.color
            self.pixel_object[pixel_len - cur_pix - 1] = self.color
        else:
            self.pixel_object[cur_pix] = self._start_col
            self.pixel_object[pixel_len - cur_pix - 1] = self._end_col

        if self.draw_count % len(self.pixel_object) == 0:
            self.color = hsv_to_rgb(random.randint(0, 360), 1, 1)
            self.on_cycle_complete()

def blend(controller: Controller, color):
    pixels = controller.pixels
    num_pixels = controller.num_pixels

    # The color wheel repeats infinetly... in the positive
    # So we add 256 to the color to make sure we get a positive number when we subtract _quart
    color = color + 256


    for i in range(num_pixels):
        if i < num_pixels // 2:
            pixels[i] = start_col
            pixels[num_pixels-i-1] = end_col
        else:
            pixels[i] = color
            pixels[num_pixels-i-1] = color

        pixels.show()