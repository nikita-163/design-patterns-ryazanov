"""Тесты задачи 11-03 «Простые множители»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_03_prime_factors.py"


def prime_factors():
    return get_function(load_module(TASK), "prime_factors")


def test_100():
    assert prime_factors()(100) == [2, 2, 5, 5]


def test_prime():
    assert prime_factors()(13) == [13]


def test_84():
    assert prime_factors()(84) == [2, 2, 3, 7]
