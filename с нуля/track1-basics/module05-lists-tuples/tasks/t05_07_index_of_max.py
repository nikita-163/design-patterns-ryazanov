"""
Задача 05-07. Где максимум

Прочитайте числа через пробел (гарантируется хотя бы одно) и выведите
индекс первого максимального числа. Нумерация с нуля.

Пример
------
Ввод:
3 7 10 4 10
Вывод:
2
"""

# TODO: найдите индекс первого максимума (строгое сравнение >)
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))

best_index = 0
for i in range(len(numbers)):
    if numbers[i] > numbers[best_index]:
        best_index = i

print(best_index)

