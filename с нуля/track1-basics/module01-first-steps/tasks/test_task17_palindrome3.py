"""Тесты задачи 17 ★ «Палиндром из трёх цифр»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task17_palindrome3.py"


def test_palindrome_true():
    assert out_lines(run_script(TASK, "121\n")) == ["True"]


def test_palindrome_false():
    assert out_lines(run_script(TASK, "123\n")) == ["False"]


def test_palindrome_757():
    assert out_lines(run_script(TASK, "757\n")) == ["True"]
