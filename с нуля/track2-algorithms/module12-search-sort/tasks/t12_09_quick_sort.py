"""
Задача 12-09 ★. Быстрая сортировка

Напишите функцию quick_sort(items), которая сортирует список быстрой
сортировкой: выберите опорный элемент (например, первый), разложите
остальные на «меньшие», «равные», «большие» и рекурсивно отсортируйте
крайние части. Встроенные sort/sorted запрещены.

Примеры
--------
quick_sort([5, 2, 9, 1]) → [1, 2, 5, 9]
"""


def quick_sort(items):
    # TODO: опорный элемент + три списка + рекурсия
    if len(items) <= 1:
        return items[:]
    pivot = items[0]
    less = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
