"""Тесты задачи 11-17 ★ «Гипотеза Гольдбаха»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_17_goldbach.py"


def goldbach():
    return get_function(load_module(TASK), "goldbach")


def test_4():
    assert goldbach()(4) == (2, 2)


def test_10():
    assert goldbach()(10) == (3, 7)


def test_26():
    assert goldbach()(26) == (3, 23)
