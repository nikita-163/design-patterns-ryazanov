"""Тесты задачи 04 «Четыре действия»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task04_arith.py"


def test_arith_7_3():
    assert out_lines(run_script(TASK, "7\n3\n")) == ["10", "4", "21", "2.333"]


def test_arith_10_4():
    assert out_lines(run_script(TASK, "10\n4\n")) == ["14", "6", "40", "2.5"]


def test_arith_negative():
    assert out_lines(run_script(TASK, "-8\n2\n")) == ["-6", "-10", "-16", "-4.0"]
