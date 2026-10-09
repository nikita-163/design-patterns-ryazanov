"""Тесты задачи 12-13 «Убрать повторы за один проход»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_13_dedupe_sorted.py"


def dedupe_sorted():
    return get_function(load_module(TASK), "dedupe_sorted")


def test_dedupe():
    assert dedupe_sorted()([1, 1, 2, 3, 3, 3]) == [1, 2, 3]


def test_empty_and_single():
    assert dedupe_sorted()([]) == []
    assert dedupe_sorted()([5]) == [5]


def test_words():
    assert dedupe_sorted()(["а", "а", "б"]) == ["а", "б"]
