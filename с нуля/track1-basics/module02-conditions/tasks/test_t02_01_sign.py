"""Тесты задачи 02-01 «Знак числа»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_01_sign.py"


def test_positive():
    assert out_lines(run_script(TASK, "5\n")) == ["положительное"]


def test_negative():
    assert out_lines(run_script(TASK, "-3\n")) == ["отрицательное"]


def test_zero():
    assert out_lines(run_script(TASK, "0\n")) == ["ноль"]
