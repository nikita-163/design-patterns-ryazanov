"""Тесты задачи 04-10 «Есть ли цифра»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_10_has_digit.py"


def test_has_digit_true():
    assert out_lines(run_script(TASK, "abc1\n")) == ["True"]


def test_has_digit_false():
    assert out_lines(run_script(TASK, "abc\n")) == ["False"]


def test_has_digit_start():
    assert out_lines(run_script(TASK, "5 пять\n")) == ["True"]
