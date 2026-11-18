"""
Задача 11-04. Простые числа до N

Напишите функцию primes_up_to(n), которая возвращает список всех простых
чисел от 2 до n включительно. Способ на выбор: перебор делителей
или решето Эратосфена.

Примеры
--------
primes_up_to(10) → [2, 3, 5, 7]
primes_up_to(2)  → [2]
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


def primes_up_to(n):
    # TODO: перебор или решето
    return [x for x in range(2, n + 1) if is_prime(x)]
