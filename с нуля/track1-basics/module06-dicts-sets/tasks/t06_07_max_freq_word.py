"""
Задача 06-07. Самое частое слово

Прочитайте предложение и выведите самое часто встречающееся слово.
Гарантируется, что такое слово ровно одно.

Пример
------
Ввод:
a b a c a b
Вывод:
a
"""

# TODO: посчитайте частоты и найдите слово-максимум
counts = {}
for word in input().split():
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

best_word = ''
best_count = 0
for word, count in counts.items():
    if count > best_count:
        best_word = word
        best_count = count

print(best_word)

