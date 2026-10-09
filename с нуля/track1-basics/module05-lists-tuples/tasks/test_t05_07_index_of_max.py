"""Тесты задачи 05-07 «Где максимум»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_07_index_of_max.py"


def test_first_max():
    assert out_lines(run_script(TASK, "3 7 10 4 10\n")) == ["2"]


def test_single():
    assert out_lines(run_script(TASK, "5\n")) == ["0"]


def test_all_descending():
    assert out_lines(run_script(TASK, "-1 -5 -3\n")) == ["0"]
