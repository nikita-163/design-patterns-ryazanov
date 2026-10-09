"""Тесты задачи 11-06 «Все делители»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_06_divisors.py"


def divisors():
    return get_function(load_module(TASK), "divisors")


def test_12():
    assert divisors()(12) == [1, 2, 3, 4, 6, 12]


def test_prime():
    assert divisors()(7) == [1, 7]


def test_1():
    assert divisors()(1) == [1]
