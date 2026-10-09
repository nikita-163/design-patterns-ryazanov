"""Тесты задачи 03 «Сумма двух чисел»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task03_sum.py"


def test_sum_small():
    assert out_lines(run_script(TASK, "2\n3\n")) == ["5"]


def test_sum_negative():
    assert out_lines(run_script(TASK, "-10\n42\n")) == ["32"]
