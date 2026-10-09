"""Тесты задачи 03-12 «Простое число»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_12_prime_check.py"


def test_prime_7():
    assert out_lines(run_script(TASK, "7\n")) == ["True"]


def test_prime_2():
    assert out_lines(run_script(TASK, "2\n")) == ["True"]


def test_prime_97():
    assert out_lines(run_script(TASK, "97\n")) == ["True"]


def test_not_prime_9():
    assert out_lines(run_script(TASK, "9\n")) == ["False"]


def test_not_prime_100():
    assert out_lines(run_script(TASK, "100\n")) == ["False"]
