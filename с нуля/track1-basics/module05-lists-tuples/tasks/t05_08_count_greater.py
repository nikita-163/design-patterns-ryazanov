"""
Задача 05-08. Больше, чем k

Прочитайте строку с числами через пробел, затем отдельной строкой —
целое число k. Выведите, сколько элементов списка больше k.

Пример
------
Ввод:
4 8 15 16
10
Вывод:
2
"""

# TODO: посчитайте элементы, большие k
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))
k = int(input())

count = 0
for x in numbers:
    if x > k:
        count += 1

print(count)

