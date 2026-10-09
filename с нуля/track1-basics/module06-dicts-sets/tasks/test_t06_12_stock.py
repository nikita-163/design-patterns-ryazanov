"""Тесты задачи 06-12 «Склад»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_12_stock.py"


def test_stock_basic():
    assert out_lines(
        run_script(TASK, "2\nсахар 10\nмука 5\n2\nсахар -3\nмука 7\n")
    ) == ["сахар: 7", "мука: 12"]


def test_stock_negative_ops():
    assert out_lines(
        run_script(TASK, "1\nхлеб 8\n3\nхлеб -2\nхлеб -3\nхлеб 5\n")
    ) == ["хлеб: 8"]


def test_stock_no_ops():
    assert out_lines(
        run_script(TASK, "2\nчай 3\nкофе 1\n0\n")
    ) == ["чай: 3", "кофе: 1"]
