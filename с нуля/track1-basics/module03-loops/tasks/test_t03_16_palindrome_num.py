"""Тесты задачи 03-16 ★ «Число-палиндром»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_16_palindrome_num.py"


def test_palindrome_12321():
    assert out_lines(run_script(TASK, "12321\n")) == ["True"]


def test_not_palindrome_123():
    assert out_lines(run_script(TASK, "123\n")) == ["False"]


def test_palindrome_single():
    assert out_lines(run_script(TASK, "7\n")) == ["True"]


def test_not_palindrome_10():
    assert out_lines(run_script(TASK, "10\n")) == ["False"]


def test_palindrome_1001():
    assert out_lines(run_script(TASK, "1001\n")) == ["True"]
