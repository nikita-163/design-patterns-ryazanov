"""Тесты задачи 02-04 «Наибольшее из трёх»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_04_max3.py"


def test_middle_is_max():
    assert out_lines(run_script(TASK, "3\n9\n1\n")) == ["9"]


def test_all_equal():
    assert out_lines(run_script(TASK, "7\n7\n7\n")) == ["7"]


def test_negatives():
    assert out_lines(run_script(TASK, "-1\n-5\n-3\n")) == ["-1"]


def test_last_is_max():
    assert out_lines(run_script(TASK, "10\n20\n30\n")) == ["30"]
