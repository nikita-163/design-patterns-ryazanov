"""Тесты задачи 03-17 ★ «Второй максимум»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_17_second_max.py"


def test_second_max_5():
    assert out_lines(run_script(TASK, "5\n3\n9\n1\n7\n5\n")) == ["7"]


def test_second_max_desc():
    assert out_lines(run_script(TASK, "4\n10\n2\n8\n4\n")) == ["8"]


def test_second_max_two():
    assert out_lines(run_script(TASK, "2\n1\n2\n")) == ["1"]
