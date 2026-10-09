"""Тесты задачи 06-04 «Общие числа»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_04_set_intersection.py"


def test_intersection_basic():
    assert out_lines(run_script(TASK, "1 3 5 7\n3 7 9\n")) == ["3 7"]


def test_intersection_empty():
    assert out_lines(run_script(TASK, "1 2\n3 4\n")) == []


def test_intersection_unsorted_input():
    assert out_lines(run_script(TASK, "9 1 5\n5 9 2\n")) == ["5 9"]
