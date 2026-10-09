"""Тесты задачи 11-09 «Шаги Коллатца»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t11_09_collatz_steps.py"


def collatz_steps():
    return get_function(load_module(TASK), "collatz_steps")


def test_one():
    assert collatz_steps()(1) == 0


def test_six():
    assert collatz_steps()(6) == 8


def test_27():
    assert collatz_steps()(27) == 111
