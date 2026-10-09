"""Тесты задачи 06-06 «Частоты букв»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_06_letter_freq.py"


def test_letter_freq_mama():
    assert out_lines(run_script(TASK, "мама\n")) == ["а: 2", "м: 2"]


def test_letter_freq_case():
    assert out_lines(run_script(TASK, "Аа\n")) == ["а: 2"]


def test_letter_freq_phrase():
    assert out_lines(run_script(TASK, "око\n")) == ["к: 1", "о: 2"]
