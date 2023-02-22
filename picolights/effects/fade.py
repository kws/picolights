from adafruit_led_animation.animation import Animation


def _fade(color: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(c - (c / 4) for c in color)

class Fade(Animation):

    on_cycle_complete_supported = True

    def draw(self):
        self.pixel_object[:] = [_fade(p) for p in self.pixel_object]
        
        if sum(sum(p) for p in self.pixel_object) == 0:
            self.cycle_complete = True


