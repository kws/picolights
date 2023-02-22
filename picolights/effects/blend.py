from adafruit_led_animation.animation import Animation
from picolights.colors import rgb_to_hsv, hsv_to_rgb

_fraq = 360 / 6


class Blend(Animation):

    on_cycle_complete_supported = True

    def _set_color(self, color):
        h, s, v = rgb_to_hsv(*color)
        self._start_col = hsv_to_rgb(h - _fraq, s, v)
        self._end_col = hsv_to_rgb(h + _fraq, s, v)
        super()._set_color(color)


    def draw(self):
        pixel_len = len(self.pixel_object)
        cur_pix = (self.draw_count - 1) % pixel_len

        if cur_pix >= pixel_len / 2:
            self.pixel_object[cur_pix] = self.color
            self.pixel_object[pixel_len - cur_pix - 1] = self.color
        else:
            self.pixel_object[cur_pix] = self._start_col
            self.pixel_object[pixel_len - cur_pix - 1] = self._end_col

        if self.draw_count % len(self.pixel_object) == 0:
            self.cycle_complete = True
