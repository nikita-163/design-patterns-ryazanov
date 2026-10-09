"""Тесты задачи 03-06 «Сколько чисел кратны семи»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_06_div7_count.py"


def test_count_50():
    assert out_lines(run_script(TASK, "50\n")) == ["7"]


def test_count_7():
    assert out_lines(run_script(TASK, "7\n")) == ["1"]


def test_count_6():
    assert out_lines(run_script(TASK, "6\n")) == ["0"]


def test_count_100():
    assert out_lines(run_script(TASK, "100\n")) == ["14"]
