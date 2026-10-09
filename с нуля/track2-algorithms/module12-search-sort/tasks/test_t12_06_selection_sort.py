"""Тесты задачи 12-06 «Сортировка выбором»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_06_selection_sort.py"


def selection_sort():
    return get_function(load_module(TASK), "selection_sort")


def test_simple():
    assert selection_sort()([3, 1, 2]) == [1, 2, 3]


def test_duplicates():
    assert selection_sort()([9, 1, 9]) == [1, 9, 9]


def test_empty_and_single():
    assert selection_sort()([]) == []
    assert selection_sort()([4]) == [4]


def test_source_not_modified():
    source = [2, 1]
    selection_sort()(source)
    assert source == [2, 1]
