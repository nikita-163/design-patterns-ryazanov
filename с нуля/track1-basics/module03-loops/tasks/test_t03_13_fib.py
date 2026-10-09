"""Тесты задачи 03-13 «Числа Фибоначчи»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_13_fib.py"


def test_fib_8():
    assert out_lines(run_script(TASK, "8\n")) == ["0 1 1 2 3 5 8 13"]


def test_fib_1():
    assert out_lines(run_script(TASK, "1\n")) == ["0"]


def test_fib_2():
    assert out_lines(run_script(TASK, "2\n")) == ["0 1"]


def test_fib_10():
    assert out_lines(run_script(TASK, "10\n")) == ["0 1 1 2 3 5 8 13 21 34"]
