"""Тесты задачи 12-14 «K-й по величине»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_14_kth_smallest.py"


def kth_smallest():
    return get_function(load_module(TASK), "kth_smallest")


def test_second():
    assert kth_smallest()([7, 1, 5, 3], 2) == 3


def test_first():
    assert kth_smallest()([9, 2], 1) == 2


def test_last():
    assert kth_smallest()([7, 1, 5, 3], 4) == 7
