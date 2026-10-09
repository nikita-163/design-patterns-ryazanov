"""Тесты задачи 03-01 «Сумма от 1 до N»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_01_sum_n.py"


def test_sum_5():
    assert out_lines(run_script(TASK, "5\n")) == ["15"]


def test_sum_1():
    assert out_lines(run_script(TASK, "1\n")) == ["1"]


def test_sum_100():
    assert out_lines(run_script(TASK, "100\n")) == ["5050"]
