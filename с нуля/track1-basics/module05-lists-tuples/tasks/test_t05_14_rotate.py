"""Тесты задачи 05-14 «Циклический сдвиг»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_14_rotate.py"


def test_rotate_2():
    assert out_lines(run_script(TASK, "1 2 3 4 5\n2\n")) == ["4 5 1 2 3"]


def test_rotate_0():
    assert out_lines(run_script(TASK, "1 2 3\n0\n")) == ["1 2 3"]


def test_rotate_full():
    assert out_lines(run_script(TASK, "1 2 3\n3\n")) == ["1 2 3"]
