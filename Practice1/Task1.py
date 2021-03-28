import math

def task1(x,y,z):
    return "{:e}".format((abs(pow(z, 6)) + pow(x, 8)/2)/(pow(z, 3) - pow(y, 7) + 51) - math.sqrt(math.log(x) + 77 * pow(x, 3) +67 ) + math.sqrt((66*pow(z,2)+23*pow(x, 7))/(pow(x, 5)) - math.tan(x)))

print(task1(36, -15, -60))
print(task1(15, -11, 92))
