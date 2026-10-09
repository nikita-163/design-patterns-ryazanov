"""Тесты задачи 03-05 «Чётные на отрезке»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_05_even_between.py"


def test_even_3_10():
    assert out_lines(run_script(TASK, "3\n10\n")) == ["4", "6", "8", "10"]


def test_even_1_5():
    assert out_lines(run_script(TASK, "1\n5\n")) == ["2", "4"]


def test_even_single_odd():
    assert out_lines(run_script(TASK, "7\n7\n")) == []


def test_even_empty_range():
    assert out_lines(run_script(TASK, "2\n1\n")) == []
