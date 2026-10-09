"""Тесты задачи 05-06 «Только чётные»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_06_evens.py"


def test_evens_6():
    assert out_lines(run_script(TASK, "1 2 3 4 5 6\n")) == ["2 4 6"]


def test_evens_none():
    assert out_lines(run_script(TASK, "1 3 5\n")) == []


def test_evens_negative():
    assert out_lines(run_script(TASK, "-4 -3 0\n")) == ["-4 0"]
