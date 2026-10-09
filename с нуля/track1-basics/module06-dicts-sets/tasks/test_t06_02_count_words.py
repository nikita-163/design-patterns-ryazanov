"""Тесты задачи 06-02 «Частоты слов»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_02_count_words.py"


def test_count_mama():
    assert out_lines(run_script(TASK, "мама мыла раму мама\n")) == [
        "мама 2",
        "мыла 1",
        "раму 1",
    ]


def test_count_single():
    assert out_lines(run_script(TASK, "привет\n")) == ["привет 1"]


def test_count_repeats():
    assert out_lines(run_script(TASK, "а б а б а\n")) == [
        "а 3",
        "б 2",
    ]
