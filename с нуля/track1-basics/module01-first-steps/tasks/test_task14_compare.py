"""Тесты задачи 14 «Сравнения»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task14_compare.py"


def test_compare_equal():
    assert out_lines(run_script(TASK, "5\n5\n")) == ["False", "False", "True"]


def test_compare_less():
    assert out_lines(run_script(TASK, "3\n8\n")) == ["False", "True", "False"]


def test_compare_greater():
    assert out_lines(run_script(TASK, "10\n-1\n")) == ["True", "False", "False"]
