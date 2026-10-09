"""Тесты задачи 02-05 «Проверка пароля»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_05_password.py"


def test_correct_password():
    assert out_lines(run_script(TASK, "python123\n")) == ["доступ разрешён"]


def test_wrong_password():
    assert out_lines(run_script(TASK, "qwerty\n")) == ["доступ запрещён"]


def test_case_matters():
    assert out_lines(run_script(TASK, "Python123\n")) == ["доступ запрещён"]
