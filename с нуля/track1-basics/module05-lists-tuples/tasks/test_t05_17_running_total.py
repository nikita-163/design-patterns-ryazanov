"""Тесты задачи 05-17 ★ «Частичные суммы»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_17_running_total.py"


def test_running_4():
    assert out_lines(run_script(TASK, "1 2 3 4\n")) == ["1 3 6 10"]


def test_running_single():
    assert out_lines(run_script(TASK, "5\n")) == ["5"]


def test_running_signed():
    assert out_lines(run_script(TASK, "2 -2 2\n")) == ["2 0 2"]
