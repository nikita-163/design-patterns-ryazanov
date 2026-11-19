"""
Задача 12-08 ★. Сортировка слиянием

Напишите функцию merge_sort(items), которая сортирует список рекурсивной
сортировкой слиянием: список делится пополам, части сортируются рекурсивно
и сливаются (слияние — как в задаче 12-07). Базовый случай: список длины
0–1 уже отсортирован. Встроенные sort/sorted запрещены.

Примеры
--------
merge_sort([5, 2, 9, 1]) → [1, 2, 5, 9]
"""


def merge(a, b):
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


def merge_sort(items):
    # TODO: база случая; деление пополам; рекурсия; слияние
    if len(items) <= 1:
        return items[:]
    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return merge(left, right)
