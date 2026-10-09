"""Тесты задачи 04-09 «Каждое слово с заглавной»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_09_capitalize_words.py"


def test_capitalize_three_words():
    assert out_lines(run_script(TASK, "привет большой мир\n")) == [
        "Привет Большой Мир"
    ]


def test_capitalize_one_word():
    assert out_lines(run_script(TASK, "привет\n")) == ["Привет"]


def test_capitalize_mixed():
    assert out_lines(run_script(TASK, "один два\n")) == ["Один Два"]
