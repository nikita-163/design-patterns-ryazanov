"""Тесты задачи 05-05 «Список наоборот»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_05_reverse_list.py"


def test_reverse_3():
    assert out_lines(run_script(TASK, "1 2 3\n")) == ["3 2 1"]


def test_reverse_single():
    assert out_lines(run_script(TASK, "9\n")) == ["9"]


def test_reverse_palindrome():
    assert out_lines(run_script(TASK, "1 2 1\n")) == ["1 2 1"]
