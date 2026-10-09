"""Тесты задачи 04-05 «Строка задом наперёд»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_05_reverse.py"


def test_reverse_russian():
    assert out_lines(run_script(TASK, "привет\n")) == ["тевирп"]


def test_reverse_palindrome():
    assert out_lines(run_script(TASK, "казак\n")) == ["казак"]


def test_reverse_single():
    assert out_lines(run_script(TASK, "а\n")) == ["а"]
