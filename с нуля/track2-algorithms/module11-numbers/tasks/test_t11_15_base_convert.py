"""Тесты задачи 11-15 ★ «В любую систему счисления»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_15_base_convert.py"


def base_convert():
    return get_function(load_module(TASK), "base_convert")


def test_hex():
    assert base_convert()(255, 16) == "FF"


def test_binary():
    assert base_convert()(10, 2) == "1010"


def test_seven():
    assert base_convert()(7, 7) == "10"


def test_octal():
    assert base_convert()(8, 8) == "10"
