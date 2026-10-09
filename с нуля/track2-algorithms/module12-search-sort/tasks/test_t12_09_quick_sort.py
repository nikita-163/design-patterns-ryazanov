"""Тесты задачи 12-09 ★ «Быстрая сортировка»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_09_quick_sort.py"


def quick_sort():
    return get_function(load_module(TASK), "quick_sort")


def test_four():
    assert quick_sort()([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_duplicates():
    assert quick_sort()([2, 2, 1, 1]) == [1, 1, 2, 2]


def test_empty_and_single():
    assert quick_sort()([]) == []
    assert quick_sort()([3]) == [3]


def test_source_not_modified():
    source = [2, 1]
    quick_sort()(source)
    assert source == [2, 1]
