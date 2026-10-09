"""Тесты задачи 11-12 «В римскую запись»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_12_roman_encode.py"


def roman_encode():
    return get_function(load_module(TASK), "roman_encode")


def test_9():
    assert roman_encode()(9) == "IX"


def test_58():
    assert roman_encode()(58) == "LVIII"


def test_1994():
    assert roman_encode()(1994) == "MCMXCIV"


def test_3999():
    assert roman_encode()(3999) == "MMMCMXCIX"
