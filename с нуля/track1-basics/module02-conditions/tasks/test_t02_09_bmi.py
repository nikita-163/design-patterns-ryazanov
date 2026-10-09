"""Тесты задачи 02-09 «Категория ИМТ»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_09_bmi.py"


def test_normal():
    assert out_lines(run_script(TASK, "70\n1.75\n")) == ["норма"]


def test_underweight():
    assert out_lines(run_script(TASK, "45\n1.6\n")) == ["недостаточный"]


def test_overweight():
    assert out_lines(run_script(TASK, "85\n1.75\n")) == ["избыточный"]


def test_obese():
    assert out_lines(run_script(TASK, "110\n1.7\n")) == ["ожирение"]
