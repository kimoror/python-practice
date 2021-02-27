import math


def f12(x):
    if x < -53:
        return math.log(pow(math.exp, x) - 93 * x - 44) - 78 * pow(x, 6)
    elif -53 <= x < 41:
        return math.tan(pow(x, 7)) - 82 * pow(x, 3)
    elif 41 <= x < 114:
        return pow((96 * pow(x, 7) + pow(x, 8) / 63), 3) - 37 * pow(x, 4)
    elif 114 <= x < 168:
        return pow(x, 4) - pow(x, 5)
    elif x >= 168:
        return 69 * pow(x, 5) - 45 * x
