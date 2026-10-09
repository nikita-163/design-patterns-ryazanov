"""Тесты задачи 04-03 «Сколько слов»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_03_word_count.py"


def test_three_words():
    assert out_lines(run_script(TASK, "один два   три\n")) == ["3"]


def test_one_word():
    assert out_lines(run_script(TASK, "привет\n")) == ["1"]


def test_extra_spaces():
    assert out_lines(run_script(TASK, "  один   два  \n")) == ["2"]
