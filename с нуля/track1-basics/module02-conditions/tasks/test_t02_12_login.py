"""Тесты задачи 02-12 «Вход по логину и паролю»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_12_login.py"


def test_ok():
    assert out_lines(run_script(TASK, "admin\nqwerty\n")) == ["вход выполнен"]


def test_wrong_password():
    assert out_lines(run_script(TASK, "admin\n123\n")) == [
        "неверный логин или пароль"
    ]


def test_wrong_login():
    assert out_lines(run_script(TASK, "root\nqwerty\n")) == [
        "неверный логин или пароль"
    ]
