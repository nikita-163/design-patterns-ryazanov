"""Тесты задачи 03-15 «Лестница из звёздочек»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_15_star_triangle.py"


def test_triangle_4():
    assert out_lines(run_script(TASK, "4\n")) == ["*", "**", "***", "****"]


def test_triangle_1():
    assert out_lines(run_script(TASK, "1\n")) == ["*"]


def test_triangle_3():
    assert out_lines(run_script(TASK, "3\n")) == ["*", "**", "***"]
