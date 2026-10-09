"""Тесты задачи 12-08 ★ «Сортировка слиянием»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_08_merge_sort.py"


def merge_sort():
    return get_function(load_module(TASK), "merge_sort")


def test_four():
    assert merge_sort()([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_duplicates_and_reverse():
    assert merge_sort()([3, 3, 1]) == [1, 3, 3]
    assert merge_sort()([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_and_single():
    assert merge_sort()([]) == []
    assert merge_sort()([6]) == [6]


def test_source_not_modified():
    source = [2, 1]
    merge_sort()(source)
    assert source == [2, 1]
