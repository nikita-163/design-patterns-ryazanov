"""Тесты задачи 04-14 «Шифр Цезаря»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_14_caesar.py"


def test_caesar_simple():
    assert out_lines(run_script(TASK, "1\nabc\n")) == ["bcd"]


def test_caesar_wrap():
    assert out_lines(run_script(TASK, "2\nxyz\n")) == ["zab"]


def test_caesar_words():
    assert out_lines(run_script(TASK, "3\nhello world\n")) == ["khoor zruog"]


def test_caesar_zero_shift():
    assert out_lines(run_script(TASK, "0\nabc\n")) == ["abc"]
