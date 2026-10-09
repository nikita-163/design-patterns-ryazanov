"""Тесты задачи 06 «Цельсий → Фаренгейт»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task06_c2f.py"


def test_c2f_body_temperature():
    assert out_lines(run_script(TASK, "36.6\n")) == ["97.9"]


def test_c2f_zero():
    assert out_lines(run_script(TASK, "0\n")) == ["32.0"]


def test_c2f_boiling():
    assert out_lines(run_script(TASK, "100\n")) == ["212.0"]


def test_c2f_negative():
    assert out_lines(run_script(TASK, "-40\n")) == ["-40.0"]
