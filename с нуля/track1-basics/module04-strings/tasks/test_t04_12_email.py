"""Тесты задачи 04-12 «Проверка e-mail»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t04_12_email.py"


def test_valid_email():
    assert out_lines(run_script(TASK, "ivan@mail.ru\n")) == ["True"]


def test_no_at():
    assert out_lines(run_script(TASK, "ivanmail.ru\n")) == ["False"]


def test_at_first():
    assert out_lines(run_script(TASK, "@mail.ru\n")) == ["False"]


def test_no_dot_after_at():
    assert out_lines(run_script(TASK, "ivan@ru\n")) == ["False"]


def test_two_at():
    assert out_lines(run_script(TASK, "ivan@mail@ru\n")) == ["False"]
