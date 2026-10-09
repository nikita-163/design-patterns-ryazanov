"""Тесты задачи 05-01 «Построчно»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_01_print_lines.py"


def test_three_numbers():
    assert out_lines(run_script(TASK, "3 7 1\n")) == ["3", "7", "1"]


def test_single():
    assert out_lines(run_script(TASK, "42\n")) == ["42"]


def test_negatives():
    assert out_lines(run_script(TASK, "-5 10\n")) == ["-5", "10"]
