# Practice2


# How to print string with int
num1 = 34
print(f'I have {num1} dollar')

# Массив сылочный тип данных
a = [1, 2]
b = a
b[0] = 5
print(a[0])

# Работа c файлами
file_write = open("Data.txt", 'w')
file_write.write("Hello world")  # Заново перезаписать файл
file_write.close()

# Максимальное количества повторений одного слова в романе война и мир
file_read = open("59495692.txt", 'r')
text = file_read.read()
lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']  # и т.д.
lst = []

for word in text.lower().split():
    if not word in lst_no:
        _word = word
        if word[-1] in lst_no:
            _word = _word[:-1]
        if word[0] in lst_no:
            _word = _word[1:]
        lst.append(_word)

_dict = dict()
for word in lst:
    _dict[word] = _dict.get(word, 0) + 1

_list = []
for key, value in _dict.items():
    _list.append((value, key))
    _list.sort(reverse=True)


for freq, word in _list[0:10]:
    print(f'{word:>10} count: {freq:>3}')
file_read.close()