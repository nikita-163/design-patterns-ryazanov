"""Тесты задачи 11-05 «Число-палиндром»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_05_is_palindrome_num.py"


def is_palindrome_num():
    return get_function(load_module(TASK), "is_palindrome_num")


def test_palindrome():
    assert is_palindrome_num()(12321) is True


def test_not_palindrome():
    assert is_palindrome_num()(123) is False


def test_single():
    assert is_palindrome_num()(7) is True


def test_trailing_zero():
    assert is_palindrome_num()(10) is False
