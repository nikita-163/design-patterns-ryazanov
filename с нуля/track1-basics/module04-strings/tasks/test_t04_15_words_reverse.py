"""Тесты задачи 04-15 «Слова в обратном порядке»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_15_words_reverse.py"


def test_reverse_words_three():
    assert out_lines(run_script(TASK, "один два три\n")) == ["три два один"]


def test_reverse_words_one():
    assert out_lines(run_script(TASK, "привет\n")) == ["привет"]


def test_reverse_words_two():
    assert out_lines(run_script(TASK, "hello world\n")) == ["world hello"]
