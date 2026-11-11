"""
Задача 06-17 ★. Сумма пары

Прочитайте строку с числами через пробел, затем отдельной строкой — целое
число target. Найдите два элемента списка, сумма которых равна target,
и выведите их индексы (нумерация с нуля) через пробел: «i j», где i < j.
Гарантируется, что подходящая пара ровно одна.

Пример
------
Ввод:
2 7 11 15
9
Вывод:
0 1
"""

# TODO: найдите пару индексов с нужной суммой
numbers = []
for p in input().split():
    numbers.append(int(p))
target = int(input())

seen = {}
for i in range(len(numbers)):
    need = target - numbers[i]
    if need in seen:
        print(seen[need], i)
        break
    seen[numbers[i]] = i

