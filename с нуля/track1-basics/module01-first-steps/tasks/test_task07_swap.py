"""Тесты задачи 07 «Обмен значений»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "task07_swap.py"


def test_swap_words():
    assert out_lines(run_script(TASK, "левый\nправый\n")) == [
        "до: левый правый",
        "после: правый левый",
    ]


def test_swap_numbers_as_text():
    assert out_lines(run_script(TASK, "1\n2\n")) == [
        "до: 1 2",
        "после: 2 1",
    ]
