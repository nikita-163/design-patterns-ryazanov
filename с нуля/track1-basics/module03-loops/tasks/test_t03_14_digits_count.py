"""Тесты задачи 03-14 «Сколько цифр в числе»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_14_digits_count.py"


def test_digits_12345():
    assert out_lines(run_script(TASK, "12345\n")) == ["5"]


def test_digits_single():
    assert out_lines(run_script(TASK, "7\n")) == ["1"]


def test_digits_1000():
    assert out_lines(run_script(TASK, "1000\n")) == ["4"]


def test_digits_987654():
    assert out_lines(run_script(TASK, "987654\n")) == ["6"]
