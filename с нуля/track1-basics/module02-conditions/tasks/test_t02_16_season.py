"""Тесты задачи 02-16 «Время года»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_16_season.py"


def test_winter():
    assert out_lines(run_script(TASK, "12\n")) == ["зима"]


def test_january_winter():
    assert out_lines(run_script(TASK, "1\n")) == ["зима"]


def test_spring():
    assert out_lines(run_script(TASK, "4\n")) == ["весна"]


def test_summer():
    assert out_lines(run_script(TASK, "7\n")) == ["лето"]


def test_autumn():
    assert out_lines(run_script(TASK, "10\n")) == ["осень"]


def test_error():
    assert out_lines(run_script(TASK, "13\n")) == ["ошибка"]


def test_zero_error():
    assert out_lines(run_script(TASK, "0\n")) == ["ошибка"]
