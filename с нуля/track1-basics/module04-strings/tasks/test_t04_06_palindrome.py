"""Тесты задачи 04-06 «Фраза-палиндром»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_06_palindrome.py"


def test_rose_palindrome():
    assert out_lines(run_script(TASK, "А роза упала на лапу Азора\n")) == ["True"]


def test_not_palindrome():
    assert out_lines(run_script(TASK, "привет\n")) == ["False"]


def test_argentina_palindrome():
    assert out_lines(run_script(TASK, "Аргентина манит негра\n")) == ["True"]
