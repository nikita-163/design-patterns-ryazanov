"""Тесты задачи 06-11 «Только в первой»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_11_set_difference.py"


def test_difference_basic():
    assert out_lines(run_script(TASK, "1 3 5 7\n3 7\n")) == ["1 5"]


def test_difference_empty():
    assert out_lines(run_script(TASK, "2 4\n2 4 6\n")) == []


def test_difference_unsorted():
    assert out_lines(run_script(TASK, "9 1 3\n3\n")) == ["1 9"]
