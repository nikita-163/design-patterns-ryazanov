"""Тесты задачи 02-17 ★ «Билет в кино»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_17_cinema.py"


def test_child_evening_session():
    # 300 → половина (150) → минус 20% = 120
    assert out_lines(run_script(TASK, "10\n15\n")) == ["120.0"]


def test_adult_evening_session():
    # 300 → минус 20% = 240
    assert out_lines(run_script(TASK, "25\n15\n")) == ["240.0"]


def test_child_late_session():
    # 300 → половина = 150
    assert out_lines(run_script(TASK, "10\n20\n")) == ["150.0"]


def test_adult_late_session():
    # скидок нет
    assert out_lines(run_script(TASK, "25\n20\n")) == ["300.0"]
