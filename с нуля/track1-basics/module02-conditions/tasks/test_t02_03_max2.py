"""Тесты задачи 02-03 «Большее из двух»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_03_max2.py"


def test_second_bigger():
    assert out_lines(run_script(TASK, "3\n9\n")) == ["9"]


def test_first_bigger():
    assert out_lines(run_script(TASK, "10\n2\n")) == ["10"]


def test_equal():
    assert out_lines(run_script(TASK, "5\n5\n")) == ["5"]


def test_negatives():
    assert out_lines(run_script(TASK, "-7\n-2\n")) == ["-2"]
