"""Тесты задачи 11-14 «Двоичная запись»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_14_binary_str.py"


def binary_str():
    return get_function(load_module(TASK), "binary_str")


def test_5():
    assert binary_str()(5) == "101"


def test_10():
    assert binary_str()(10) == "1010"


def test_1():
    assert binary_str()(1) == "1"


def test_255():
    assert binary_str()(255) == "11111111"
