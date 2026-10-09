"""Тесты задачи 12 «Чек со скидкой»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task12_receipt.py"


def test_receipt_with_discount():
    assert out_lines(run_script(TASK, "19.99\n7\n12\n")) == [
        "Стоимость: 139.93",
        "Скидка: 16.79",
        "К оплате: 123.14",
    ]


def test_receipt_no_discount():
    assert out_lines(run_script(TASK, "250\n2\n0\n")) == [
        "Стоимость: 500.0",
        "Скидка: 0.0",
        "К оплате: 500.0",
    ]
