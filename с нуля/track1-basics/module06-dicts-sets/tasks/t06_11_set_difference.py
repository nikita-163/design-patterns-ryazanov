"""
Задача 06-11. Только в первой

Прочитайте две строки с числами через пробел. Выведите числа, которые есть
в первой строке, но отсутствуют во второй, — по возрастанию, через пробел.
Если таких нет, ничего не выводите.

Пример
------
Ввод:
1 3 5 7
3 7
Вывод:
1 5
"""

# TODO: разность множеств, сортировка, вывод
first = set()
for p in input().split():
    first.add(int(p))

second = set()
for p in input().split():
    second.add(int(p))

result = []
for x in sorted(first - second):
    result.append(str(x))

if result:
    print(' '.join(result))

