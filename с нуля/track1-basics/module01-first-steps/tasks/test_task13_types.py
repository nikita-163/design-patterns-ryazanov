"""Тесты задачи 13 «Типы и преобразования»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task13_types.py"

EXPECTED = ["<class 'str'>", "<class 'int'>", "<class 'float'>"]


def test_types_42():
    assert out_lines(run_script(TASK, "42\n")) == EXPECTED


def test_types_7():
    assert out_lines(run_script(TASK, "7\n")) == EXPECTED
