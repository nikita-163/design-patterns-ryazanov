"""
Задача 05-03. Максимум и минимум

Прочитайте числа через пробел (гарантируется хотя бы одно) и выведите
две строки:

    Максимум: <наибольшее число>
    Минимум: <наименьшее число>

Функции max/min не использовать. За начальное значение берите первый
элемент списка.

Пример
------
Ввод:
3 -7 10 4
Вывод:
Максимум: 10
Минимум: -7
"""

# TODO: найдите максимум и минимум перебором
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))

biggest = numbers[0]
smallest = numbers[0]
for x in numbers:
    if x > biggest:
        biggest = x
    if x < smallest:
        smallest = x

print(f'Максимум: {biggest}')
print(f'Минимум: {smallest}')

