"""
Задача 11-13. Из римской записи

Напишите функцию roman_decode(s), которая переводит строку с римской
записью числа (валидной) обратно в целое число. Правило вычитания: буква,
меньшая следующей, вычитается (IV = 4).

Примеры
--------
roman_decode("IX")      → 9
roman_decode("MCMXCIV") → 1994
"""


ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_decode(s):
    # TODO: обход слева направо с сравнением соседних букв
    total = 0
    for i in range(len(s)):
        value = ROMAN[s[i]]
        if i + 1 < len(s) and value < ROMAN[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
