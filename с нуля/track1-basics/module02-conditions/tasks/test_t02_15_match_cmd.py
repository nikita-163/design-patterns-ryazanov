"""Тесты задачи 02-15 «Команды (match)»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_15_match_cmd.py"


def test_start():
    assert out_lines(run_script(TASK, "старт\n")) == ["запуск"]


def test_stop():
    assert out_lines(run_script(TASK, "стоп\n")) == ["остановка"]


def test_unknown():
    assert out_lines(run_script(TASK, "перезагрузка\n")) == [
        "неизвестная команда"
    ]
