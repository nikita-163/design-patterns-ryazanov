"""Тесты задачи 02-06 «Високосный год»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_06_leap.py"


def test_2024_leap():
    assert out_lines(run_script(TASK, "2024\n")) == ["True"]


def test_1900_not_leap():
    assert out_lines(run_script(TASK, "1900\n")) == ["False"]


def test_2000_leap():
    assert out_lines(run_script(TASK, "2000\n")) == ["True"]


def test_2023_not_leap():
    assert out_lines(run_script(TASK, "2023\n")) == ["False"]
