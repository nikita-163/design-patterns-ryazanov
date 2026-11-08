"""
Задача 05-13. Соседние равные

Прочитайте числа через пробел и выведите True, если в списке есть два
соседних равных элемента, иначе False.

Пример
------
Ввод:
1 2 2 3
Вывод:
True
"""

# TODO: переберите соседние пары (a[i] и a[i+1]) и сравните
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))

found = False
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        found = True
        break

print(found)

