"""Тесты задачи 06-17 ★ «Сумма пары»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_17_two_sum.py"


def test_two_sum_classic():
    assert out_lines(run_script(TASK, "2 7 11 15\n9\n")) == ["0 1"]


def test_two_sum_middle():
    assert out_lines(run_script(TASK, "3 2 4\n6\n")) == ["1 2"]


def test_two_sum_equal_values():
    assert out_lines(run_script(TASK, "3 3\n6\n")) == ["0 1"]
