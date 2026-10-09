"""Тесты задачи 01 «Привет, мир!»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task01_hello.py"


def test_hello():
    assert out_lines(run_script(TASK)) == ["Привет, мир!"]
