"""Тесты задачи 11-11 «Чётные числа Фибоначчи»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_11_fib_even_sum.py"


def fib_even_sum():
    return get_function(load_module(TASK), "fib_even_sum")


def test_100():
    assert fib_even_sum()(100) == 44


def test_1000():
    assert fib_even_sum()(1000) == 798


def test_below_2():
    assert fib_even_sum()(1) == 0
