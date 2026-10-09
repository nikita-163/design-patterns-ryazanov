"""Тесты задачи 04-01 «Приветствие капсом»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_01_shout.py"


def test_shout_russian():
    assert out_lines(run_script(TASK, "иван\n")) == ["Привет, ИВАН!"]


def test_shout_latin():
    assert out_lines(run_script(TASK, "anna\n")) == ["Привет, ANNA!"]


def test_shout_mixed_case():
    assert out_lines(run_script(TASK, "Пётр\n")) == ["Привет, ПЁТР!"]
