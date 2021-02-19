# Ответы на теоретические вопросы находятся в файле AnswersOnQuestions.md

"""
Попробуйте составить код для решения следующих задач. Из арифметических операций можно использовать только явно
указанные и в указанном количестве. Входным аргументом является переменная x.
"""


def no_multiply(x):
    if x == 12:
        return 3 + 3 + 3 + 3
    elif x == 16:
        return 4 + 4 + 4 + 4
    elif x == 15:
        return 6 + 6 + 6 - 2 - 1
    elif x == 29:
        return 5 + 5 + 5 + 5 + 5 + 5 - 1


print(f'Умножение 1 на {no_multiply(29)}: {no_multiply(29)}')



"""
# Некто попытался реализовать "наивную" функцию умножения с помощью сложений. К сожалению, в коде много ошибок.
# Сможете ли вы их исправить?
"""


def naive_mul(x, y):
    r = 0
    for i in range(y):
        r += x
    return r


def naive_mul_test():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("naive_mul_test is passed")


naive_mul_test()



"""
# Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного умножения в столбик.
# Добавьте автоматическое тестирование,как в случае с naive_mul.
"""


def fast_mul(x, y):
    # if x == 1:
    #     return y
    # if y == 1:
    #     return x
    res = 0
    while x >= 1:
        if x == 0 or y == 0:
            return 0
        elif x % 2 == 0:
            y *= 2
            x //= 2
        elif x % 2 != 0:
            res += y
            y *= 2
            x //= 2
    return res


def fast_mul_test():
    for x in range(101):
        for y in range(101):
            assert fast_mul(x, y) == x * y
    print("fast_mull_test is passed")


fast_mul_test()


# Реализуйте аналогичную функцию для возведения в степень
def fast_pow(base, degree, mul=1):
    if degree == 0 and base == 0:
        return 1
    # elif degree == 1:
    #     return base
    if degree == 0:
        return mul
    elif base == 0:
        return 0
    elif base == 1:
        return 1
    if degree % 2 != 0:
        mul *= base
    return fast_pow(base * base, degree // 2, mul)


def fast_pow_test():
    for x in range(101):
        for y in range(101):
            assert fast_pow(x, y) == x ** y
    print("fast_mull_test is passed")


fast_pow_test()
