"""Тесты задачи 11-10 «Число Армстронга»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_10_armstrong.py"


def armstrong():
    return get_function(load_module(TASK), "armstrong")


def test_153():
    assert armstrong()(153) is True


def test_9474():
    assert armstrong()(9474) is True


def test_10():
    assert armstrong()(10) is False
