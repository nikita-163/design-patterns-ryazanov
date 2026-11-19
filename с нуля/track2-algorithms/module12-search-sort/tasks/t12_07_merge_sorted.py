"""
Задача 12-07. Слияние упорядоченных списков

Напишите функцию merge_sorted(a, b), которая сливает два отсортированных
списка в один отсортированный за один проход (два указателя). Встроенные
sort/sorted запрещены.

Примеры
--------
merge_sorted([1, 4], [2, 3, 5]) → [1, 2, 3, 4, 5]
"""


def merge_sorted(a, b):
    # TODO: два индекса; хвосты дописать в конец
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
