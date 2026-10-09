"""Тесты задачи 03-09 «Перевёрнутое число»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_09_reverse_num.py"


def test_reverse_1234():
    assert out_lines(run_script(TASK, "1234\n")) == ["4321"]


def test_reverse_leading_zeros():
    assert out_lines(run_script(TASK, "107\n")) == ["701"]


def test_reverse_single():
    assert out_lines(run_script(TASK, "5\n")) == ["5"]


def test_reverse_1000():
    assert out_lines(run_script(TASK, "1000\n")) == ["1"]
