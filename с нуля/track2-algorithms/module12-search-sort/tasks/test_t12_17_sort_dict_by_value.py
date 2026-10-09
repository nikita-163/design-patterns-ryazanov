"""Тесты задачи 12-17 ★ «Словарь по значению»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_17_sort_dict_by_value.py"


def sort_dict_by_value():
    return get_function(load_module(TASK), "sort_dict_by_value")


def test_desc_with_tie():
    assert sort_dict_by_value()({"а": 2, "б": 3, "в": 2}) == [
        ("б", 3),
        ("а", 2),
        ("в", 2),
    ]


def test_single():
    assert sort_dict_by_value()({"x": 1}) == [("x", 1)]
