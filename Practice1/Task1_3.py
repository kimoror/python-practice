import math


def f13(n, m):
    loop1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            loop1 += (math.fabs(j) + j ** 6)

    loop2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            loop2 += (j ** 3 - i ** 7 + 51)

    return loop1 - 22 * loop2
