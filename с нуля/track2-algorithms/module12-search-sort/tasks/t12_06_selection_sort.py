"""
Задача 12-06. Сортировка выбором

Напишите функцию selection_sort(items), которая возвращает НОВЫЙ
отсортированный список: на каждом шаге ищите минимум в неотсортированном
остатке и ставьте его на место. Встроенные sort/sorted запрещены.

Примеры
--------
selection_sort([3, 1, 2]) → [1, 2, 3]
"""


def selection_sort(items):
    # TODO: копия; поиск минимума в остатке + обмен
    result = items[:]
    for i in range(len(result) - 1):
        min_index = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result
