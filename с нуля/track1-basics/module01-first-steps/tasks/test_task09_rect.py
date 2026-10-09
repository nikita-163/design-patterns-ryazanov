"""Тесты задачи 09 «Прямоугольник»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task09_rect.py"


def test_rect_whole():
    assert out_lines(run_script(TASK, "2.5\n5\n")) == [
        "Площадь: 12.5",
        "Периметр: 15.0",
    ]


def test_rect_fractional():
    assert out_lines(run_script(TASK, "3.3\n4.7\n")) == [
        "Площадь: 15.51",
        "Периметр: 16.0",
    ]
