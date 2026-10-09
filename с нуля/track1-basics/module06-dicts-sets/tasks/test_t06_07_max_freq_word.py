"""Тесты задачи 06-07 «Самое частое слово»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_07_max_freq_word.py"


def test_max_freq_a():
    assert out_lines(run_script(TASK, "a b a c a b\n")) == ["a"]


def test_max_freq_last():
    assert out_lines(run_script(TASK, "x y y\n")) == ["y"]


def test_max_freq_russian():
    assert out_lines(run_script(TASK, "мир труд мир\n")) == ["мир"]
