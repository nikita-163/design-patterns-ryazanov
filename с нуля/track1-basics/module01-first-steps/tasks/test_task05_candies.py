"""Тесты задачи 05 «Конфеты и упаковки»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task05_candies.py"


def test_candies_100_7():
    assert out_lines(run_script(TASK, "100\n7\n")) == [
        "Полных упаковок: 14",
        "Осталось конфет: 2",
    ]


def test_candies_exact():
    assert out_lines(run_script(TASK, "50\n5\n")) == [
        "Полных упаковок: 10",
        "Осталось конфет: 0",
    ]


def test_candies_less_than_pack():
    assert out_lines(run_script(TASK, "3\n10\n")) == [
        "Полных упаковок: 0",
        "Осталось конфет: 3",
    ]
