"""Тесты задачи 06-08 «Какие цифры есть в строке»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_08_digits_set.py"


def test_digits_mixed():
    assert out_lines(run_script(TASK, "a1b23c1\n")) == ["1 2 3"]


def test_digits_none():
    assert out_lines(run_script(TASK, "abc\n")) == []


def test_digits_order():
    assert out_lines(run_script(TASK, "9x5x9\n")) == ["5 9"]
