"""Тесты задачи 05-08 «Больше, чем k»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_08_count_greater.py"


def test_greater_10():
    assert out_lines(run_script(TASK, "4 8 15 16\n10\n")) == ["2"]


def test_greater_none():
    assert out_lines(run_script(TASK, "1 2 3\n5\n")) == ["0"]


def test_greater_negative():
    assert out_lines(run_script(TASK, "-5 0 5\n-6\n")) == ["3"]
