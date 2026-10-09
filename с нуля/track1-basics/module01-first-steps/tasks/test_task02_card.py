"""Тесты задачи 02 «Визитка»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task02_card.py"

EXPECTED = ["Имя: Иван", "Группа: ПИ-101", "Город: Москва"]


def test_card():
    assert out_lines(run_script(TASK)) == EXPECTED
