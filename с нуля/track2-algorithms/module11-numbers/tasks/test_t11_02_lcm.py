"""Тесты задачи 11-02 «НОК»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_02_lcm.py"


def lcm():
    return get_function(load_module(TASK), "lcm")


def test_lcm_4_6():
    assert lcm()(4, 6) == 12


def test_lcm_coprimes():
    assert lcm()(7, 13) == 91
