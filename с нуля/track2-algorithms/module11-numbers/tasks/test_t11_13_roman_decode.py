"""Тесты задачи 11-13 «Из римской записи»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_13_roman_decode.py"


def roman_decode():
    return get_function(load_module(TASK), "roman_decode")


def test_ix():
    assert roman_decode()("IX") == 9


def test_mcmxciv():
    assert roman_decode()("MCMXCIV") == 1994


def test_lviii():
    assert roman_decode()("LVIII") == 58
