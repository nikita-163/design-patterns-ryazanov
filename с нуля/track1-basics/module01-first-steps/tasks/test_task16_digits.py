"""Тесты задачи 16 «Сумма цифр трёхзначного числа»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task16_digits.py"


def test_digits_472():
    assert out_lines(run_script(TASK, "472\n")) == ["Сумма цифр: 13"]


def test_digits_900():
    assert out_lines(run_script(TASK, "900\n")) == ["Сумма цифр: 9"]


def test_digits_101():
    assert out_lines(run_script(TASK, "101\n")) == ["Сумма цифр: 2"]
