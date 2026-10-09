"""Тесты задачи 12-15 «Куда вставить»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_15_insert_position.py"


def insert_position():
    return get_function(load_module(TASK), "insert_position")


def test_middle():
    assert insert_position()([1, 3, 5], 4) == 2


def test_beginning():
    assert insert_position()([1, 3, 5], 0) == 0


def test_end():
    assert insert_position()([1, 3, 5], 9) == 3


def test_existing_left():
    assert insert_position()([1, 3, 3, 5], 3) == 1
