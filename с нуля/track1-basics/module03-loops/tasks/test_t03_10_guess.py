"""Тесты задачи 03-10 «Угадай число»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_10_guess.py"


def test_guess_three_attempts():
    assert out_lines(run_script(TASK, "10\n50\n42\n")) == [
        "больше",
        "меньше",
        "угадал",
    ]


def test_guess_first_try():
    assert out_lines(run_script(TASK, "42\n")) == ["угадал"]


def test_guess_around():
    assert out_lines(run_script(TASK, "41\n43\n42\n")) == [
        "больше",
        "меньше",
        "угадал",
    ]
