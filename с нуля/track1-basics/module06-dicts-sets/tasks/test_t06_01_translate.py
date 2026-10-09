"""Тесты задачи 06-01 «Мини-словарь»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_01_translate.py"


def test_translate_cat():
    assert out_lines(run_script(TASK, "cat\n")) == ["кот"]


def test_translate_house():
    assert out_lines(run_script(TASK, "house\n")) == ["дом"]


def test_translate_missing():
    assert out_lines(run_script(TASK, "moon\n")) == ["нет в словаре"]
