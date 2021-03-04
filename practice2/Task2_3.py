import copy
from typing import List


table1 = [
    ['', 'Выполнено', '+7 328 204-38-39', '17%', '17%'],
    ['', 'Не выполнено', '+7 304 166-11-08', '34%', '34%'],
    ['', 'Выполнено', '+7 567 381-63-27', '49%', '49%'],
    ['', 'Выполнено', '+7 114 834-24-90', '95%', '95%'],
]

table2 = [
    ['', 'Не выполнено', '+7 739 139‐97‐56', '40%', '40%'],
    ['', 'Не выполнено', '+7 459 456‐73‐63', '6%', '6%'],
    ['', 'Не выполнено', '+7 083 953‐25‐50', '11%', '11%'],
    ['', 'Выполнено', '+7 542 257‐17‐32', '80%', '80%']
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
            if j is None:
                count_none += 1
        if len(i) == count_none:
            table.remove(i)
        count_none = 0


def transform(table):
    # first_column = []
    # for iter in table[0]:
    #     if iter == 'Выполнено':
    #         first_column.append('Да')
    #     else:
    #         first_column.append('Нет')
    # table[0] = first_column
    #
    # second_column = []
    # for i in table[1]:
    #     # i = i[i.find(" ") + 1:]
    #     # lis = i.split('')
    #     # print(lis[0])
    #     # i = lis[2]
    #     # i = str(i[7:])
    #     # i = i[i.find(" ") + 1:]
    #     # left_i = str(i[:6])
    #     # right_i = str(i[7:])
    #     # i = str('')
    #     # i = left_i + right_i
    #     # i = i.replace(chr(8208), chr(45))
    #     # origin_i = copy.copy(i)
    #     # i = origin_i.split(' ')[2].split('-')[0]
    #     # i += '-'+origin_i.split(' ')[2].split('-')[1]
    #     # i += origin_i.split(' ')[2].split('-')[2]
    #     # i = i.split(' ')[2].split('-')[0] + '-'+i.split(' ')[2].split('-')[1] + i.split(' ')[2].split('-')[2]
    #     second_column.append(i)
    # table[1] = second_column
    #
    # third_column = []
    # for i in table[3]:
    #     i = i[:-1]
    #     third_column.append(str(round(int(i)/100, 1)))
    # table[3] = third_column
    #
    # fourth_column = []
    # for i in table[2]:
    #     i = i[:-1]
    #     fourth_column.append(str(round(int(i) / 100, 1)))
    # table[2] = fourth_column
    #
    # return table
    a = [[], [], []]

    for array in table:
        if array[1] == 'Выполнено':
            a[0].append('Да')
        elif array[1] == 'Не выполнено':
            a[0].append('Нет')

        a[1].append(array[2].split(' ')[2].split('-')[0] + '-' + array[2].split(' ')[2].split('-')[1] + array[2].split(' ')[2].split('-')[2])

        tmp0 = array[3].split('%')[0]
        tmp0 = int(tmp0) / 100
        a[2].append(str(round(tmp0, 1)))


def f23(table):
    table = transpose(table)
    table = transform(table)
    table = delete_doubles(table)
    delete_none(table)
    return table


# Если сделать print, то выведет none , так как функция ничего не возвращает
print(f23(table1))
print(f23(table2))

# print(ord('‐'))