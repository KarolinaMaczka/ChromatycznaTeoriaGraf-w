import random

RADIUS = 1.5
AMOUNT = 6

RANGE_FROM = 0
RANGE_TO = 10

COLOURS = {None: '#000000', 0: '#FF0000', 1: '#FFA500', 2: '#FFFF00', 3: '#00FF00', 4: '#008000',
           5: '#00FFFF', 6: '#008080', 7: '#0000FF', 8: '#000080', 9: '#FF00FF',
           10: '#800080', 11: '#FFC0CB', 12: '#A52A2A', 13: '#D2691E', 14: '#BDB76B',
           15: '#808080', 16: '#C0C0C0', 17: '#FFFFFF', 18: '#F5DEB3', 19: '#8B4513'}


def rand(a, b):
    return random.random() * (b - a) + a
