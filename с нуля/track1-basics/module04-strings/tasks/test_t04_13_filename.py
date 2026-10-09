"""Тесты задачи 04-13 «Имя файла и расширение»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_13_filename.py"


def test_simple_file():
    assert out_lines(run_script(TASK, "report.pdf\n")) == [
        "Имя: report",
        "Расширение: pdf",
    ]


def test_two_dots():
    assert out_lines(run_script(TASK, "my.file.txt\n")) == [
        "Имя: my.file",
        "Расширение: txt",
    ]


def test_photo():
    assert out_lines(run_script(TASK, "photo.jpeg\n")) == [
        "Имя: photo",
        "Расширение: jpeg",
    ]
