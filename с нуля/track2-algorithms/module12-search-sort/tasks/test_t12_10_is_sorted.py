"""Тесты задачи 12-10 «Отсортирован ли»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_10_is_sorted.py"


def is_sorted():
    return get_function(load_module(TASK), "is_sorted")


def test_sorted_with_equal():
    assert is_sorted()([1, 2, 2, 3]) is True


def test_not_sorted():
    assert is_sorted()([1, 3, 2]) is False


def test_trivial():
    assert is_sorted()([]) is True
    assert is_sorted()([4]) is True
