"""Тесты задачи 12-01 «Линейный поиск»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_01_linear_search.py"


def linear_search():
    return get_function(load_module(TASK), "linear_search")


def test_found():
    assert linear_search()([5, 3, 7], 7) == 2


def test_first_occurrence():
    assert linear_search()([5, 3, 5], 5) == 0


def test_missing():
    assert linear_search()([5, 3, 7], 9) == -1
