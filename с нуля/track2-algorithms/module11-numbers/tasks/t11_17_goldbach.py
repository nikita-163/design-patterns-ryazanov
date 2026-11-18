"""
Задача 11-17 ★. Гипотеза Гольдбаха

Напишите функцию goldbach(n), которая для чётного n ≥ 4 возвращает кортеж
(p, q) двух простых чисел с суммой n; при нескольких вариантах берите
наименьшее p (тогда q наибольшее).

Примеры
--------
goldbach(4)  → (2, 2)
goldbach(10) → (3, 7)
goldbach(26) → (3, 23)
"""


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def goldbach(n):
    # TODO: перебор p от 2 вверх, проверка простоты p и n - p
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n - p):
            return p, n - p
