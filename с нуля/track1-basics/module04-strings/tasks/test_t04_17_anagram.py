"""Тесты задачи 04-17 ★ «Анаграммы»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_17_anagram.py"


def test_anagram_true():
    assert out_lines(run_script(TASK, "листок\nстолик\n")) == ["True"]


def test_anagram_false():
    assert out_lines(run_script(TASK, "стол\nстул\n")) == ["False"]


def test_anagram_case_insensitive():
    assert out_lines(run_script(TASK, "АВС\nвса\n")) == ["True"]
