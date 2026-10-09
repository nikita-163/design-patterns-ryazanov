"""Тесты задачи 08 «Знакомство (f-строки)»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task08_fstring.py"


def test_intro_anya():
    assert out_lines(run_script(TASK, "Аня\n19\n")) == [
        "Имя: Аня, возраст: 19",
        "Год рождения: 2007",
    ]


def test_intro_ivan():
    assert out_lines(run_script(TASK, "Иван\n35\n")) == [
        "Имя: Иван, возраст: 35",
        "Год рождения: 1991",
    ]
