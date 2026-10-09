"""Тесты задачи 05-04 «Квадраты»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_04_squares.py"


def test_squares_4():
    assert out_lines(run_script(TASK, "4\n1\n5\n-2\n3\n")) == ["1 25 4 9"]


def test_squares_single():
    assert out_lines(run_script(TASK, "1\n7\n")) == ["49"]


def test_squares_zero():
    assert out_lines(run_script(TASK, "2\n0\n10\n")) == ["0 100"]
