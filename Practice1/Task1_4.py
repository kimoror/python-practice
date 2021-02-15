import math

def func(x):
    if x == 0:
        return 7
    else:
         return math.tan(func(x-1)) - math.sin(func(x-1)) - 23

print("{:e}".format(func(3)))
print("{:e}".format(func(9)))