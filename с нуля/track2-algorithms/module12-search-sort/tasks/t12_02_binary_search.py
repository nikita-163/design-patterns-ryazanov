"""
Задача 12-02. Бинарный поиск

Напишите функцию binary_search(items, x), которая ищет x в ОТсортированном
списке бинарным поиском и возвращает индекс или −1. Методом index
и перебором пользоваться нельзя — только деление диапазона пополам.

Примеры
--------
binary_search([1, 3, 5, 7, 9], 7) → 3
binary_search([1, 3, 5, 7, 9], 4) → -1
"""


def binary_search(items, x):
    # TODO: lo/hi/mid по шпаргалке
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == x:
            return mid
        if items[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
