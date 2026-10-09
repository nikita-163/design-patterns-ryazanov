"""Тесты задачи 05-03 «Максимум и минимум»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_03_max_min.py"


def test_max_min_mixed():
    assert out_lines(run_script(TASK, "3 -7 10 4\n")) == [
        "Максимум: 10",
        "Минимум: -7",
    ]


def test_max_min_single():
    assert out_lines(run_script(TASK, "5\n")) == [
        "Максимум: 5",
        "Минимум: 5",
    ]


def test_max_min_all_negative():
    assert out_lines(run_script(TASK, "-3 -1 -9\n")) == [
        "Максимум: -1",
        "Минимум: -9",
    ]
