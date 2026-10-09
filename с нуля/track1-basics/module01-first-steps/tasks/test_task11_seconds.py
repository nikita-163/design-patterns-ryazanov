"""Тесты задачи 11 «Часы, минуты, секунды»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task11_seconds.py"


def test_seconds_10000():
    assert out_lines(run_script(TASK, "10000\n")) == [
        "Часов: 2",
        "Минут: 46",
        "Секунд: 40",
    ]


def test_seconds_3725():
    assert out_lines(run_script(TASK, "3725\n")) == [
        "Часов: 1",
        "Минут: 2",
        "Секунд: 5",
    ]


def test_seconds_59():
    assert out_lines(run_script(TASK, "59\n")) == [
        "Часов: 0",
        "Минут: 0",
        "Секунд: 59",
    ]
