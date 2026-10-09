"""Тесты задачи 12-11 «По модулю»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_11_sorted_by_abs.py"


def sorted_by_abs():
    return get_function(load_module(TASK), "sorted_by_abs")


def test_by_abs():
    assert sorted_by_abs()([-5, 2, -1]) == [-1, 2, -5]


def test_tie_keeps_stable_order():
    # sorted устойчив: равные по ключу сохраняют взаимный порядок
    assert sorted_by_abs()([2, -2]) == [2, -2]
