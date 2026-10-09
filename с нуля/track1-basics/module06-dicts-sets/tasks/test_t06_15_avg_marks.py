"""Тесты задачи 06-15 «Средний балл»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_15_avg_marks.py"


def test_avg_marks_basic():
    assert out_lines(
        run_script(TASK, "3\nанна матем 5\nборис физика 4\nанна физика 3\n")
    ) == ["анна 4.0", "борис 4.0"]


def test_avg_marks_rounding():
    assert out_lines(
        run_script(TASK, "2\nанна матем 5\nанна физика 4\n")
    ) == ["анна 4.5"]


def test_avg_marks_three_subjects():
    assert out_lines(
        run_script(TASK, "3\nпётр а 3\nпётр б 4\nпётр в 5\n")
    ) == ["пётр 4.0"]
