"""Тесты задачи 03-02 «Обратный отсчёт»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_02_countdown.py"


def test_countdown_3():
    assert out_lines(run_script(TASK, "3\n")) == ["3", "2", "1", "Пуск"]


def test_countdown_1():
    assert out_lines(run_script(TASK, "1\n")) == ["1", "Пуск"]


def test_countdown_5():
    assert out_lines(run_script(TASK, "5\n")) == ["5", "4", "3", "2", "1", "Пуск"]
