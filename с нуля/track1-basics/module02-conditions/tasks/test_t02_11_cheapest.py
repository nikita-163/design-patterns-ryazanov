"""Тесты задачи 02-11 «Самая дешёвая цена»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_11_cheapest.py"


def test_middle_cheapest():
    assert out_lines(run_script(TASK, "250\n199\n300\n")) == ["199.0"]


def test_equal_min():
    assert out_lines(run_script(TASK, "100\n100\n90\n")) == ["90.0"]


def test_first_cheapest():
    assert out_lines(run_script(TASK, "9.99\n14.5\n10.0\n")) == ["9.99"]
