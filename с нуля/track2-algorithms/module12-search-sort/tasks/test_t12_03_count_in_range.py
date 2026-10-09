"""Тесты задачи 12-03 «Сколько в диапазоне»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_03_count_in_range.py"


def count_in_range():
    return get_function(load_module(TASK), "count_in_range")


def test_range_2_5():
    assert count_in_range()([1, 5, 3, 8, 2], 2, 5) == 3


def test_bounds_included():
    assert count_in_range()([1, 2, 3], 1, 3) == 3


def test_none():
    assert count_in_range()([10, 20], 1, 5) == 0
