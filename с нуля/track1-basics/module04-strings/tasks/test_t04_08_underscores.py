"""Тесты задачи 04-08 «Имя файла без пробелов»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_08_underscores.py"


def test_filename_spaces():
    assert out_lines(
        run_script(TASK, "мой отчёт за 2026 год.pdf\n")
    ) == ["мой_отчёт_за_2026_год.pdf"]


def test_filename_latin():
    assert out_lines(run_script(TASK, "file name.txt\n")) == ["file_name.txt"]


def test_filename_no_spaces():
    assert out_lines(run_script(TASK, "report.pdf\n")) == ["report.pdf"]
