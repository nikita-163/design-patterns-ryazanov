"""Тесты задачи 05-09 «Среднее арифметическое»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_09_average.py"


def test_average_4():
    assert out_lines(run_script(TASK, "1 2 3 4\n")) == ["2.5"]


def test_average_two():
    assert out_lines(run_script(TASK, "1 2\n")) == ["1.5"]


def test_average_same():
    assert out_lines(run_script(TASK, "5 5 5\n")) == ["5.0"]
