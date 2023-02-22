import random
from rainbowio import colorwheel
from binascii import unhexlify, hexlify
from ._names import from_color_name


def to_color(color):
    if isinstance(color, str) and not color.startswith("#"):
        color = from_color_name(color)
    if isinstance(color, str) and color.startswith("#"):
        color = color[1:]
        if len(color) == 3:
            color = color[0] * 2 + color[1] * 2 + color[2] * 2
        color = int.from_bytes(unhexlify(color), "big")
    if isinstance(color, int):
        color = (color >> 16 & 0xFF, color >> 8 & 0xFF, color & 0xFF)
    return color


def to_hex(color):
    if isinstance(color, tuple):
        color = (color[0] << 16) + (color[1] << 8) + color[2]
    return "#" + hexlify(int.to_bytes(color, 3, "big")).decode("ascii")


def random_color():
    return colorwheel(random.randint(0, 255))


def rgb_to_hsv(r: int, g: int, b:int) -> tuple[int, float, float]:
    r, g, b = r / 255, g / 255, b / 255
    c_max = max(r, g, b)
    c_min = min(r, g, b)
    delta = c_max - c_min

    if delta == 0:
        h = 0
    elif c_max == r:
        h = 60 * (((g - b) / delta) % 6)
    elif c_max == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    if c_max == 0:
        s = 0
    else:
        s = delta / c_max

    v = c_max

    return round(h), s, v


def hsv_to_rgb(h: int, s: float, v: float) -> tuple[int, int, int]:
    while h < 0:
        h += 360

    while h > 360:
        h -= 360

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return round((r + m) * 255), round((g + m) * 255), round((b + m) * 255)
