"""Тесты задачи 02-08 «Существует ли треугольник»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_08_triangle.py"


def test_right_triangle():
    assert out_lines(run_script(TASK, "3\n4\n5\n")) == ["да"]


def test_degenerate():
    assert out_lines(run_script(TASK, "1\n2\n3\n")) == ["нет"]


def test_too_long_side():
    assert out_lines(run_script(TASK, "5\n1\n1\n")) == ["нет"]
