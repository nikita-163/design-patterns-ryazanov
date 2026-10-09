"""Тесты задачи 04-04 «Инициалы»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_04_initials.py"


def test_initials_ivanov():
    assert out_lines(run_script(TASK, "Иванов Иван Иванович\n")) == ["И.И.И."]


def test_initials_petrov():
    assert out_lines(
        run_script(TASK, "Петров Пётр Петрович\n")
    ) == ["П.П.П."]


def test_initials_mixed():
    assert out_lines(
        run_script(TASK, "Сидоров Анна Олеговна\n")
    ) == ["С.А.О."]
