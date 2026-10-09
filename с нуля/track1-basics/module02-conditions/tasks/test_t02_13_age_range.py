"""Тесты задачи 02-13 «Допуск по возрасту»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_13_age_range.py"


def test_middle():
    assert out_lines(run_script(TASK, "30\n")) == ["допущен"]


def test_lower_boundary():
    assert out_lines(run_script(TASK, "18\n")) == ["допущен"]


def test_upper_boundary():
    assert out_lines(run_script(TASK, "65\n")) == ["допущен"]


def test_too_young():
    assert out_lines(run_script(TASK, "17\n")) == ["не допущен"]


def test_too_old():
    assert out_lines(run_script(TASK, "66\n")) == ["не допущен"]
