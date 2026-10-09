"""Тесты задачи 05-02 «Сумма и количество»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_02_sum_count.py"


def test_sum_count_4():
    assert out_lines(run_script(TASK, "4 8 15 16\n")) == [
        "Сумма: 43",
        "Количество: 4",
    ]


def test_sum_count_single():
    assert out_lines(run_script(TASK, "7\n")) == ["Сумма: 7", "Количество: 1"]


def test_sum_count_negatives():
    assert out_lines(run_script(TASK, "-1 -2 -3\n")) == [
        "Сумма: -6",
        "Количество: 3",
    ]
