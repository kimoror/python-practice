from typing import List


table1 = [
    ['', 'Выполнено', '+7 328 204‐38‐39', '17%', '17%', None],
    ['', 'Не выполнено', '+7 304 166‐11‐08', '34%', '34%', None],
    ['', 'Выполнено', '+7 567 381‐63‐27', '49%', '49%', None],
    ['', 'Выполнено', '+7 114 834‐24‐90', '95%', '95%', None],
]


# * - разделяет параметры в неизменяемом списке
def transpose(table):
    column_nums = 0
    y_new_table = []
    for column_total in table[0]:
        y_new_strokes = []
        for column in table:
            y_new_strokes.append(column[column_nums])
        y_new_table.append(y_new_strokes)
        column_nums += 1
    return y_new_table


def delete_doubles(table):
    temp_table = []
    for i in table:
        if i not in temp_table:
            temp_table.append(i)
    return temp_table


def delete_none(table):
    count_none = 0
    for i in table:
        for j in i:
            if j is None or j == '':
                count_none += 1
        if len(i) == count_none:
            table.remove(i)
        count_none = 0
    return table


def transform(table):
    first_column = []
    for iter in table[0]:
        if iter == 'Выполнено':
            first_column.append('Да')
        else:
            first_column.append('Нет')
    table[0] = first_column

    second_column = []
    for i in table[1]:
        i = i[i.find(" ") + 1:]
        i = i[i.find(" ") + 1:]
        left_i = i[:6]
        right_i = i[7:]
        i = ''
        i += left_i + right_i
        second_column.append(i)
    table[1] = second_column

    third_column = []
    for i in table[3]:
        i = i[:-1]
        third_column.append(str(round(float(i)/100, 1)))
    table[3] = third_column

    fourth_column = []
    for i in table[2]:
        i = i[:-1]
        fourth_column.append(str(round(float(i) / 100, 1)))
    table[2] = third_column

    return table


def f23(table):
    table = transpose(table)
    table = delete_none(table)
    table = transform(table)
    table = delete_doubles(table)
    return table


# Если сделать print, то выведет none , так как функция ничего не возвращает
print(f23(table1))
