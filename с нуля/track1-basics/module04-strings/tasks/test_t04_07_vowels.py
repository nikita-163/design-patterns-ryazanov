"""Тесты задачи 04-07 «Сколько гласных»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_07_vowels.py"


def test_vowels_hello():
    assert out_lines(run_script(TASK, "Привет, мир!\n")) == ["3"]


def test_vowels_uppercase():
    assert out_lines(run_script(TASK, "АУЕИ\n")) == ["4"]


def test_vowels_none():
    assert out_lines(run_script(TASK, "BCdfg\n")) == ["0"]
