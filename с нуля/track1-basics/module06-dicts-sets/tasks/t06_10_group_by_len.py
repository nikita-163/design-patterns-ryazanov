"""
Задача 06-10. Группировка по длине

Прочитайте слова через пробел и сгруппируйте их по длине. Выведите строки
«длина: слова через пробел» — длины по возрастанию, слова внутри группы
в порядке появления.

Пример
------
Ввод:
кот дом дерево
Вывод:
3: кот дом
6: дерево
"""

# TODO: словарь «длина → список слов», вывод по возрастанию длин
groups = {}
for word in input().split():
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

for length in sorted(groups):
    line = ' '.join(groups[length])
    print(f'{length}: {line}')

