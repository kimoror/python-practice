import json
import csv
import json2html

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

"""
i = 0
['much','code','wow'][i] # 24 символа
Out[1]:
'much'
Сократите код в строке №2 до 19 символов без использования функций.
"""
# i = 0
# print(['much'|'code'|'wow'])


'''
Реализовать утилиту командной строки для преобразования данных с сайта с результатами
проверки робота kispython в форматы csv, ascii и html. Использовать данные вашей группы из table.json.
'''
with open('table.json') as file_json:
    data = json.load(file_json)
json_data = data['data']

# to_csv
csv_file = open('file_csv.csv', 'w')
csv_writer = csv.writer(csv_file)
count = 0
for i in json_data:
    csv_writer.writerow(i)

# to ascii
ascii_writer = open('ascii.txt', 'w')
info = json.dumps(json_data, ensure_ascii=False)
ascii_writer.write(info)

# to html
html_writer = open('html.html', 'w')
html_writer.write(json2html.json2html.convert(info))

ascii_writer.close()
csv_file.close()
