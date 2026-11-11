"""
Задача 06-16 ★. Первое уникальное слово

Прочитайте слова через пробел и выведите первое слово, которое встречается
в тексте ровно один раз. Если такого нет, выведите «-».

Пример
------
Ввод:
а б а в б г
Вывод:
в
"""

# TODO: сначала посчитайте частоты, затем найдите первое слово с частотой 1
words = input().split()

counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

answer = '-'
for word in words:
    if counts[word] == 1:
        answer = word
        break

print(answer)

