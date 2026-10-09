"""Тесты задачи 04-16 ★ «Самое длинное слово»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_16_longest_word.py"


def test_longest_python():
    assert out_lines(run_script(TASK, "я учу язык python\n")) == ["python"]


def test_longest_tie_first():
    assert out_lines(run_script(TASK, "дом кот\n")) == ["дом"]


def test_longest_single():
    assert out_lines(run_script(TASK, "привет\n")) == ["привет"]
