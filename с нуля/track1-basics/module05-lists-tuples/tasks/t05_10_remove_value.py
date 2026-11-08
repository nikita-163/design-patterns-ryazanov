"""
Задача 05-10. Без числа x

Прочитайте строку с числами через пробел, затем отдельной строкой —
число x. Выведите исходные числа без вхождений x — одной строкой через
пробел, порядок сохраняется. Если после удаления ничего не осталось,
не выводите ничего.

Пример
------
Ввод:
1 2 1 3 1
1
Вывод:
2 3
"""

# TODO: соберите новый список без x и выведите его
parts = input().split()
numbers = []
for p in parts:
    numbers.append(int(p))
x = int(input())

result = []
for number in numbers:
    if number != x:
        result.append(str(number))

if result:
    print(' '.join(result))

