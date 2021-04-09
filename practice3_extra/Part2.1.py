import json
import email.utils
import matplotlib.pyplot as plt

with open('table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

days = [m['date'][:3] for m in messages]

messages = [(m['subj'].upper(), email.utils.parsedate(m['date']))  for m in messages]
#Как по времени суток распределяется активность студентов?
mes_lst = list()
for i in messages:
    mes_lst.append(i[1][3])

mes_graph = plt.figure()
plt.plot([i for i in range(24)], [mes_lst.count(i) for i in range(24)], marker='.', color='red')
plt.xlabel('Часы')
plt.ylabel('Сообщения')
plt.xticks([i for i in range(24)])
plt.show()


#Как по дням недели распределяется активность студентов?


weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.plot(weekdays, [days.count(i) for i in weekdays], marker='.', color='red')
plt.xlabel('День недели')
plt.ylabel('Сообщения')
plt.show()


#В каких группах было отправлено больше всего сообщений?

lst_t3 = list()

for i in messages:
    lst_t3.append(i[0][:3].replace(' ', ''))

mp1 = set(lst_t3) #удаляем повторяющиеся
mp1 = list(mp1)
mp1.sort()
plt.plot(mp1, [lst_t3.count(i) for i in mp1], marker='.', color='red')
plt.show()

#В каких группах было получено больше всего правильных решений?

lst2 = list()
for i in table['data']:
    if i[3] == 1:
        lst2.append(i[0])

mp2 = set(lst2)
mp2 = list(mp2)
mp2.sort()
plt.plot(mp2, [lst2.count(i) for i in mp2], marker='.', color='red')
plt.show()

#Какие задачи оказались самыми легкими, самыми сложными?

lst3 = list()
for i in table['data']:
    if i[3] == 0:
        lst3.append(i[2])

mp3 = set(lst3)
mp3 = list(mp3)
mp3.sort()
plt.plot(mp3, [lst3.count(i) for i in mp3], marker='.', color='red')
plt.show()