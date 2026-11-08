"""
Задача 05-11. Медиана

Прочитайте числа через пробел (гарантируется хотя бы одно) и выведите
медиану — средний элемент отсортированного списка. Для чётного количества
элементов — среднее двух средних (округлите до 2 знаков).

Пример
------
Ввод:
5 1 3
Вывод:
3

Ввод:
4 1 3 2
Вывод:
2.5
"""

# TODO: отсортируйте список и найдите медиану
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))

ordered = sorted(numbers)
size = len(ordered)
middle = size // 2

if size % 2 == 1:
    print(ordered[middle])
else:
    print(round((ordered[middle - 1] + ordered[middle]) / 2, 2))

