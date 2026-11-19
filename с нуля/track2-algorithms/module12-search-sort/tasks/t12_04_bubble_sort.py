"""
Задача 12-04. Пузырьковая сортировка

Напишите функцию bubble_sort(items), которая возвращает НОВЫЙ отсортированный
по возрастанию список, отсортированный пузырьком. Встроенные sort/sorted
запрещены; исходный список изменять нельзя.

Примеры
--------
bubble_sort([3, 1, 2]) → [1, 2, 3]
"""


def bubble_sort(items):
    # TODO: копия + соседние обмены по шпаргалке
    result = items[:]
    for i in range(len(result) - 1):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result
