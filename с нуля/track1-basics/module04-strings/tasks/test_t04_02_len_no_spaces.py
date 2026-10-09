"""Тесты задачи 04-02 «Длина без пробелов»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_02_len_no_spaces.py"


def test_len_with_space():
    assert out_lines(run_script(TASK, "привет мир\n")) == ["9"]


def test_len_no_spaces():
    assert out_lines(run_script(TASK, "python\n")) == ["6"]


def test_len_only_spaces():
    assert out_lines(run_script(TASK, "   \n")) == ["0"]
