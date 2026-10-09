"""Тесты задачи 02-02 «Чётное или нечётное»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_02_even.py"


def test_even():
    assert out_lines(run_script(TASK, "4\n")) == ["чётное"]


def test_odd():
    assert out_lines(run_script(TASK, "7\n")) == ["нечётное"]


def test_zero_even():
    assert out_lines(run_script(TASK, "0\n")) == ["чётное"]


def test_negative_even():
    assert out_lines(run_script(TASK, "-2\n")) == ["чётное"]
