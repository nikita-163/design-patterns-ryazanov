"""Тесты задачи 06-13 «Общие буквы»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_13_common_letters.py"


def test_common_mama_papa():
    assert out_lines(run_script(TASK, "мама\nпапа\n")) == ["а"]


def test_common_case_insensitive():
    assert out_lines(run_script(TASK, "Сон\nнос\n")) == ["н о с"]


def test_common_none():
    assert out_lines(run_script(TASK, "xyz\nабв\n")) == []
