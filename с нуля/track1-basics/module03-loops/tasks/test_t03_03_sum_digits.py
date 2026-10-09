"""Тесты задачи 03-03 «Сумма цифр числа»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_03_sum_digits.py"


def test_sum_digits_12345():
    assert out_lines(run_script(TASK, "12345\n")) == ["15"]


def test_sum_digits_single():
    assert out_lines(run_script(TASK, "7\n")) == ["7"]


def test_sum_digits_zero():
    assert out_lines(run_script(TASK, "0\n")) == ["0"]


def test_sum_digits_with_zero():
    assert out_lines(run_script(TASK, "907\n")) == ["16"]
