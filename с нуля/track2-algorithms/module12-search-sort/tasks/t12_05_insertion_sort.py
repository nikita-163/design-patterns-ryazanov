"""
Задача 12-05. Сортировка вставками

Напишите функцию insertion_sort(items), которая возвращает НОВЫЙ
отсортированный список, сортируя вставками (встроенные sort/sorted
запрещены, исходный список не менять).

Примеры
--------
insertion_sort([3, 1, 2]) → [1, 2, 3]
"""


def insertion_sort(items):
    # TODO: копия + «заталкивание» каждого элемента в отсортированную часть
    result = items[:]
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result
