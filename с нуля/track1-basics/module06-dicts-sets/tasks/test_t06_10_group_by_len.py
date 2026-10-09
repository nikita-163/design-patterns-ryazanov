"""Тесты задачи 06-10 «Группировка по длине»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_10_group_by_len.py"


def test_group_basic():
    assert out_lines(run_script(TASK, "кот дом дерево\n")) == [
        "3: кот дом",
        "6: дерево",
    ]


def test_group_single():
    assert out_lines(run_script(TASK, "привет\n")) == ["6: привет"]


def test_group_many():
    assert out_lines(run_script(TASK, "а бб вв а\n")) == [
        "1: а а",
        "2: бб вв",
    ]
