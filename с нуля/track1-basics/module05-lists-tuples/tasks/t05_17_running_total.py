"""
Задача 05-17 ★. Частичные суммы

Прочитайте числа через пробел и выведите их частичные суммы одной строкой
через пробел: первое число, сумма первых двух, сумма первых трёх и т.д.

Пример
------
Ввод:
1 2 3 4
Вывод:
1 3 6 10
"""

# TODO: накапливайте сумму и собирайте результаты
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))

total = 0
sums = []
for x in numbers:
    total += x
    sums.append(str(total))

print(' '.join(sums))

