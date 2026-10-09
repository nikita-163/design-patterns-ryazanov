"""Тесты задачи 11-07 «Совершенное число»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_07_perfect_number.py"


def perfect_number():
    return get_function(load_module(TASK), "perfect_number")


def test_6():
    assert perfect_number()(6) is True


def test_28():
    assert perfect_number()(28) is True


def test_12():
    assert perfect_number()(12) is False
