"""Тесты задачи 05-12 «Без повторов»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_12_unique.py"


def test_unique_dups():
    assert out_lines(run_script(TASK, "1 2 1 3 2 4\n")) == ["1 2 3 4"]


def test_unique_no_dups():
    assert out_lines(run_script(TASK, "5 6 7\n")) == ["5 6 7"]


def test_unique_same():
    assert out_lines(run_script(TASK, "9 9 9\n")) == ["9"]
