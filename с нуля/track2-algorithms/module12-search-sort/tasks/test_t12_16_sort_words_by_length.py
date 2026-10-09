"""Тесты задачи 12-16 ★ «Слова по длине»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_16_sort_words_by_length.py"


def sort_words_by_length():
    return get_function(load_module(TASK), "sort_words_by_length")


def test_length_then_alpha():
    assert sort_words_by_length()(["б", "аа", "в"]) == ["б", "в", "аа"]


def test_same_length():
    assert sort_words_by_length()(["дом", "кот"]) == ["дом", "кот"]
