import math


def f14(x):
    if x == 0:
        return 7
    else:
        return math.tan(f14(x - 1)) - math.sin(f14(x - 1)) - 23
