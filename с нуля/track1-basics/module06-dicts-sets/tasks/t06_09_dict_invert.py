"""
Задача 06-09. Обратный словарь

Прочитайте целое число n, затем n строк «английское русское». Постройте
обратный словарь (русское → английское) и выведите его пары «ключ: значение»
построчно, отсортировав по ключу (русские слова — по алфавиту).

Пример
------
Ввод:
3
one один
two два
three три
Вывод:
два: two
один: one
три: three
"""

# TODO: постройте обратный словарь и выведите по sorted-ключам
n = int(input())

inverted = {}
for _ in range(n):
    english, russian = input().split()
    inverted[russian] = english

for russian in sorted(inverted):
    print(f'{russian}: {inverted[russian]}')

