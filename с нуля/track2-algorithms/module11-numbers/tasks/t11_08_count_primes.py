"""
Задача 11-08. Сколько простых на отрезке

Напишите функцию count_primes(a, b), которая возвращает количество простых
чисел на отрезке от a до b включительно (a и b могут быть любыми целыми).

Примеры
--------
count_primes(1, 10)   → 4   (2, 3, 5, 7)
count_primes(10, 20)  → 4   (11, 13, 17, 19)
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


def count_primes(a, b):
    # TODO: перебор чисел отрезка с проверкой простоты
    count = 0
    for x in range(a, b + 1):
        if is_prime(x):
            count += 1
    return count
