"""Тесты задачи 11-08 «Сколько простых на отрезке»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_08_count_primes.py"


def count_primes():
    return get_function(load_module(TASK), "count_primes")


def test_1_10():
    assert count_primes()(1, 10) == 4


def test_10_20():
    assert count_primes()(10, 20) == 4


def test_no_primes():
    assert count_primes()(24, 28) == 0
