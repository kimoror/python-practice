"""
Преобразовать элементы списка s из строковой в числовую форму.
"""
def str_to_int(s):
    return [int(it) for it in s]


"""
Подсчитать количество различных элементов в последовательности s.
"""
def calc_diff_elem(s):
    return len(set(s))


"""
Обратить последовательность s без использования функций.
"""
def revert(s):
    return s[::-1]


"""
Выдать список индексов, на которых найден элемент x в последовательности s.
"""
def index_list(x, s):
    return [i for i in range(len(s)) if x == s[i]]


"""
Сложить элементы списка s с четными индексами.
"""
def sum_even(s):
    return sum(s[1::2])

"""
Найти строку максимальной длины в списке строк s.
"""
def max_len(s):
    return max([len(str) for str in s])

"""
Тесты
"""
assert str_to_int(["34", "234", "91", "89"]) == [34, 234, 91, 89]
assert calc_diff_elem([34, 5, 33, 34, 44, 5]) == 4
assert revert([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert index_list(5, [45, 5, 1, 5, 9, 4, 5]) == [1, 3, 6]
assert sum_even([1, 2, 3, 4]) == 6
assert max_len(["ads", "dddd", "d", "ddddd"]) == 5
