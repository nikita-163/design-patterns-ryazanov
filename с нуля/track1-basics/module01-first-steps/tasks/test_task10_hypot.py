"""Тесты задачи 10 «Гипотенуза»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task10_hypot.py"


def test_hypot_3_4():
    assert out_lines(run_script(TASK, "3\n4\n")) == ["Гипотенуза: 5.0"]


def test_hypot_unit():
    assert out_lines(run_script(TASK, "1\n1\n")) == ["Гипотенуза: 1.414"]


def test_hypot_fractional():
    assert out_lines(run_script(TASK, "1.5\n2.5\n")) == ["Гипотенуза: 2.915"]
