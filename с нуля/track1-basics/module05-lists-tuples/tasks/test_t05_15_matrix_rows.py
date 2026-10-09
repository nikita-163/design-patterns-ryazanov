"""Тесты задачи 05-15 «Суммы строк матрицы»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_15_matrix_rows.py"


def test_matrix_2x3():
    assert out_lines(run_script(TASK, "2\n3\n1 2 3\n4 5 6\n")) == ["6", "15"]


def test_matrix_1x1():
    assert out_lines(run_script(TASK, "1\n1\n7\n")) == ["7"]


def test_matrix_negatives():
    assert out_lines(run_script(TASK, "2\n2\n-1 -2\n3 4\n")) == ["-3", "7"]
