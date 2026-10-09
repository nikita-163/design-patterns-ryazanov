"""Тесты задачи 11-01 «НОД»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_01_gcd.py"


def gcd():
    return get_function(load_module(TASK), "gcd")


def test_gcd_12_18():
    assert gcd()(12, 18) == 6


def test_gcd_coprimes():
    assert gcd()(7, 13) == 1


def test_gcd_with_zero():
    assert gcd()(0, 5) == 5
