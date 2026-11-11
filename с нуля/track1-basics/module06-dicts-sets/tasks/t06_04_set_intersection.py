"""
Задача 06-04. Общие числа

Прочитайте две строки с числами через пробел. Выведите числа, которые
встречаются в обеих строках, — по возрастанию, через пробел. Если общих
чисел нет, не выводите ничего.

Пример
------
Ввод:
1 3 5 7
3 7 9
Вывод:
3 7
"""

# TODO: пересечение двух множеств, сортировка, вывод
first = set()
for p in input().split():
    first.add(int(p))

second = set()
for p in input().split():
    second.add(int(p))

result = []
for x in sorted(first & second):
    result.append(str(x))

if result:
    print(' '.join(result))

