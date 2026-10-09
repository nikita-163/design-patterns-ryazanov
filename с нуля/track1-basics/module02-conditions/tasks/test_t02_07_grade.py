"""Тесты задачи 02-07 «Оценка по баллам»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_07_grade.py"


def test_excellent():
    assert out_lines(run_script(TASK, "95\n")) == ["отлично"]


def test_good_boundary():
    assert out_lines(run_script(TASK, "75\n")) == ["хорошо"]


def test_satisfactory():
    assert out_lines(run_script(TASK, "60\n")) == ["удовлетворительно"]


def test_failed():
    assert out_lines(run_script(TASK, "59\n")) == ["неудовлетворительно"]
