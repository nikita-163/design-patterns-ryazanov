"""Тесты задачи 05-16 ★ «Транспонирование матрицы»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_16_transpose.py"


def test_transpose_2x3():
    assert out_lines(run_script(TASK, "2\n3\n1 2 3\n4 5 6\n")) == [
        "1 4",
        "2 5",
        "3 6",
    ]


def test_transpose_square():
    assert out_lines(run_script(TASK, "2\n2\n1 2\n3 4\n")) == ["1 3", "2 4"]


def test_transpose_row():
    assert out_lines(run_script(TASK, "1\n3\n7 8 9\n")) == ["7", "8", "9"]
