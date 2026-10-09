"""Тесты задачи 05-10 «Без числа x»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_10_remove_value.py"


def test_remove_ones():
    assert out_lines(run_script(TASK, "1 2 1 3 1\n1\n")) == ["2 3"]


def test_remove_nothing():
    assert out_lines(run_script(TASK, "4 5 6\n7\n")) == ["4 5 6"]


def test_remove_all():
    assert out_lines(run_script(TASK, "9 9\n9\n")) == []
