import json
import csv
import random
import os

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
i = 0
print("muchcodewow"[:i + 4])

'''
Напишите функцию generate_groups(), которая генерирует (не просто выдает готовый) список всех названий групп в том виде,
который используется в выпадающем списке на сайте с результатами от робота kispython.
'''


def generate_groups(group_name):
    return f'{group_name[1]}{group_name[5:7]}'


'''
Реализуйте с помощью zip() функцию transpose() для транспонирования матрицы.
'''


def transpose(x):
    return [list(i) for i in zip(*x)]


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

'''
Реализуйте генератор докладов по цифровой экономике
'''
text = [
    ['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,',
     'Следовательно,', 'Соответственно,', 'Вместе с тем,', 'С другой стороны,'],
    ['парадигма цифровой экономики', 'контекст цифровой трансформации',
     'диджитализация бизнес-процессов', 'прагматичный подход к цифровым платформам', 'совокупность сквозных технологий',
     'программа прорывных исследований', 'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data'],
    ['открывает новые возможности для', 'выдвигает новые требования', 'несёт в себе риски', 'расширяет горизонты',
     'заставляет искать варианты',
     'не оставляет шанса для', 'повышает вероятность', 'обостряет проблему'],
    ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта',
     'компрометации конфиденциальных',
     'универсальной коммодитизации', 'несанкционированной кастомизации', 'нормативного регулирования',
     'практического применения'],
    ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных экспериментов.',
     'государственно-частных партнёрств.', 'цифровых следов граждан.', 'нежелательных последствий.',
     'внезапных открытий.']
]


def generate_report():
    return ' '.join(random.choice(i) for i in text)


print(generate_report())

'''
Реализуйте генератор случайных данных ФИО. Список распространенных имен позволяется скачать из интернета. 
Фамилии необходимо генерировать самостоятельно.
'''
first_names = ['Аарон', 'Абрам', 'Аваз', 'Аввакум', 'Август', 'Августа', 'Августин', 'Августина',
               'Авдей', 'Авдий', 'Авдотья', 'Авигея', 'Авксентий', 'Авраам', 'Аврор', 'Аврора', 'Автандил', 'Автоноя', ]

father_names = 'ФЫВАПРОЛДЖЭЙЦУКЕНГШЩЗХЯЧСМИТБЮ'

second_names_one = ['Фрот', 'Врот', 'Крот', 'Фров', 'Жрон', 'Фрог', 'Врат', ]
second_names_two = ['ау', 'уе', 'суий', 'ов', 'ло', 'ая', 'а', ]


def generate_fio():
    return f'{random.choice(first_names)} {random.choice(father_names)}. {random.choice(second_names_one)}{random.choice(second_names_two)}'


for _ in range(10):
    print(generate_fio())

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

'''
Написать утилиту командной строки, формирующую дерево каталогов и файлов с 
учетом вложенности и начиная с заданного пути. Результат должен быть выдан в виде текста в формате graphviz.
'''


def get_files(input):
    for fd, subfds, fns in os.walk(input):
        fd = f'\"{fd}\"'
        print('subgraph ' + fd + ' {')
        for fn in fns:
            fn = f'\"{fn}\"'
            yield os.path.join(fd, fn)
        print('}')


## now this will print all full paths

print('digraph G {')
for fn in get_files("./"):
    fn = fn.replace('\\', '->')
    print(f'{fn};')
print('}')