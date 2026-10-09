"""Тесты задачи 15 «Банковский вклад»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task15_deposit.py"


def test_deposit_10k_7_5():
    assert out_lines(run_script(TASK, "10000\n7\n5\n")) == [
        "Итоговая сумма: 14025.52"
    ]


def test_deposit_1500_4_10():
    assert out_lines(run_script(TASK, "1500\n4\n10\n")) == [
        "Итоговая сумма: 2220.37"
    ]


def test_deposit_zero_years():
    assert out_lines(run_script(TASK, "1234.5\n10\n0\n")) == [
        "Итоговая сумма: 1234.5"
    ]
