"""Тесты задачи 06-16 ★ «Первое уникальное слово»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_16_first_unique.py"


def test_first_unique_middle():
    assert out_lines(run_script(TASK, "а б а в б г\n")) == ["в"]


def test_first_unique_none():
    assert out_lines(run_script(TASK, "а а\n")) == ["-"]


def test_first_unique_single():
    assert out_lines(run_script(TASK, "x\n")) == ["x"]


def test_first_unique_two():
    assert out_lines(run_script(TASK, "а а б\n")) == ["б"]
