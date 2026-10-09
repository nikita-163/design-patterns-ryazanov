"""Тесты задачи 11-16 ★ «Сумма цифр факториала»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_16_factorial_digit_sum.py"


def factorial_digit_sum():
    return get_function(load_module(TASK), "factorial_digit_sum")


def test_10():
    assert factorial_digit_sum()(10) == 27


def test_100():
    assert factorial_digit_sum()(100) == 648
