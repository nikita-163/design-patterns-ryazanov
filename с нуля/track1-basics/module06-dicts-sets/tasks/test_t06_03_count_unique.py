"""Тесты задачи 06-03 «Сколько различных»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_03_count_unique.py"


def test_unique_5():
    assert out_lines(run_script(TASK, "3 1 3 2 1\n")) == ["3"]


def test_unique_all_same():
    assert out_lines(run_script(TASK, "7 7 7\n")) == ["1"]


def test_unique_all_different():
    assert out_lines(run_script(TASK, "1 2 3 4\n")) == ["4"]
