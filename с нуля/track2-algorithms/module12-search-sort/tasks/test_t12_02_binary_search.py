"""Тесты задачи 12-02 «Бинарный поиск»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_02_binary_search.py"


def binary_search():
    return get_function(load_module(TASK), "binary_search")


def test_found_middle():
    assert binary_search()([1, 3, 5, 7, 9], 5) == 2


def test_found_right():
    assert binary_search()([1, 3, 5, 7, 9], 7) == 3


def test_missing():
    assert binary_search()([1, 3, 5, 7, 9], 4) == -1


def test_single():
    assert binary_search()([2], 2) == 0


def test_empty():
    assert binary_search()([], 1) == -1
