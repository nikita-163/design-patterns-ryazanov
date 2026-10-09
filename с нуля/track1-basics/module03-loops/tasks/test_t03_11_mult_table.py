"""Тесты задачи 03-11 «Таблица умножения»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_11_mult_table.py"


def test_table_7():
    out = out_lines(run_script(TASK, "7\n"))
    assert len(out) == 10
    assert out[0] == "7 x 1 = 7"
    assert out[4] == "7 x 5 = 35"
    assert out[9] == "7 x 10 = 70"


def test_table_1():
    out = out_lines(run_script(TASK, "1\n"))
    assert out[0] == "1 x 1 = 1"
    assert out[9] == "1 x 10 = 10"
