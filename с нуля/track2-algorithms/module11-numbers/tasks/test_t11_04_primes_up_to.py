"""Тесты задачи 11-04 «Простые числа до N»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_04_primes_up_to.py"


def primes_up_to():
    return get_function(load_module(TASK), "primes_up_to")


def test_up_to_10():
    assert primes_up_to()(10) == [2, 3, 5, 7]


def test_up_to_2():
    assert primes_up_to()(2) == [2]


def test_up_to_1():
    assert primes_up_to()(1) == []


def test_up_to_30():
    assert primes_up_to()(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
