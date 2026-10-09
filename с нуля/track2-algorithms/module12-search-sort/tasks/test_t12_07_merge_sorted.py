"""Тесты задачи 12-07 «Слияние упорядоченных списков»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_07_merge_sorted.py"


def merge_sorted():
    return get_function(load_module(TASK), "merge_sorted")


def test_interleaved():
    assert merge_sorted()([1, 4], [2, 3, 5]) == [1, 2, 3, 4, 5]


def test_one_empty():
    assert merge_sorted()([], [1, 2]) == [1, 2]
    assert merge_sorted()([1, 2], []) == [1, 2]


def test_duplicates():
    assert merge_sorted()([1, 2], [1, 2]) == [1, 1, 2, 2]
