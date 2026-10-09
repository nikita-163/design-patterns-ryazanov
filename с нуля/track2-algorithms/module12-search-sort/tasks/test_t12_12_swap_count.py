"""Тесты задачи 12-12 «Сколько обменов сделает пузырёк»."""
from pathlib import Path

from coursekit.loader import get_function, load_module

TASK = Path(__file__).parent / "t12_12_swap_count.py"


def swap_count():
    return get_function(load_module(TASK), "swap_count")


def test_sorted():
    assert swap_count()([1, 2, 3]) == 0


def test_reverse():
    assert swap_count()([3, 2, 1]) == 3


def test_partial():
    assert swap_count()([3, 1, 2]) == 2
