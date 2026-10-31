"""
Задача 03-17 ★. Второй максимум

Сначала поступает целое число n (n ≥ 2), затем n различных целых чисел.
Выведите второе по величине из них.

Списки и сортировку не использовать — отслеживайте два наибольших
значения по мере чтения.

Пример
------
Ввод:
5
3
9
1
7
5
Вывод:
7
"""

n = int(input())

# TODO: читайте числа и отслеживайте два максимума; выведите второй
first = int(input())
second = int(input())
if second > first:
    first, second = second, first

for _ in range(n - 2):
    x = int(input())
    if x > first:
        second = first
        first = x
    elif x > second:
        second = x

print(second)

