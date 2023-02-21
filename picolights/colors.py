import random
from rainbowio import colorwheel

def random_color():
    return colorwheel(random.randint(0, 255))