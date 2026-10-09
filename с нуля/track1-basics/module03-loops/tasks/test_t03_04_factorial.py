"""Тесты задачи 03-04 «Факториал»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_04_factorial.py"


def test_factorial_5():
    assert out_lines(run_script(TASK, "5\n")) == ["120"]


def test_factorial_0():
    assert out_lines(run_script(TASK, "0\n")) == ["1"]


def test_factorial_1():
    assert out_lines(run_script(TASK, "1\n")) == ["1"]


def test_factorial_10():
    assert out_lines(run_script(TASK, "10\n")) == ["3628800"]
