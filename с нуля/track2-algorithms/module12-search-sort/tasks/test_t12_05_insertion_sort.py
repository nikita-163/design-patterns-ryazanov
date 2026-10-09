"""Тесты задачи 12-05 «Сортировка вставками»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_05_insertion_sort.py"


def insertion_sort():
    return get_function(load_module(TASK), "insertion_sort")


def test_simple():
    assert insertion_sort()([4, 2, 5, 1]) == [1, 2, 4, 5]


def test_reverse():
    assert insertion_sort()([5, 4, 3]) == [3, 4, 5]


def test_empty_and_single():
    assert insertion_sort()([]) == []
    assert insertion_sort()([7]) == [7]


def test_source_not_modified():
    source = [3, 1]
    insertion_sort()(source)
    assert source == [3, 1]
