"""Тесты задачи 02-14 «Цвет шахматной клетки»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_14_chess_color.py"


def test_a1_white():
    assert out_lines(run_script(TASK, "1\n1\n")) == ["белая"]


def test_a2_black():
    assert out_lines(run_script(TASK, "1\n2\n")) == ["чёрная"]


def test_h8_white():
    assert out_lines(run_script(TASK, "8\n8\n")) == ["белая"]


def test_c5():
    assert out_lines(run_script(TASK, "3\n5\n")) == ["белая"]
