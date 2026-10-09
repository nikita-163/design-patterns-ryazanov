"""Тесты задачи 04-11 «Сколько раз встречается буква»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_11_count_letter.py"


def test_count_m():
    assert out_lines(run_script(TASK, "мама мыла раму\nм\n")) == ["4"]


def test_count_absent():
    assert out_lines(run_script(TASK, "привет\nя\n")) == ["0"]


def test_count_latin():
    assert out_lines(run_script(TASK, "hello world\nl\n")) == ["3"]
