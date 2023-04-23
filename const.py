import random

RADIUS = 1.5
AMOUNT = 6

RANGE_FROM = 0
RANGE_TO = 10

COLOURS = {None: "#000000", 0: "#ff0000", 1: "#00ff00", 2: "#0000ff", 3: "#f0000f", 4: "#0f00f0", 5: "#f00f00"}


def rand(a, b):
    return random.random() * (b - a) + a
