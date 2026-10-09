"""Тесты задачи 12-04 «Пузырьковая сортировка»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_04_bubble_sort.py"


def bubble_sort():
    return get_function(load_module(TASK), "bubble_sort")


def test_simple():
    assert bubble_sort()([3, 1, 2]) == [1, 2, 3]


def test_duplicates():
    assert bubble_sort()([2, 1, 2, 1]) == [1, 1, 2, 2]


def test_empty_and_single():
    assert bubble_sort()([]) == []
    assert bubble_sort()([5]) == [5]


def test_already_sorted():
    assert bubble_sort()([1, 2, 3]) == [1, 2, 3]


def test_source_not_modified():
    source = [3, 1, 2]
    bubble_sort()(source)
    assert source == [3, 1, 2]
