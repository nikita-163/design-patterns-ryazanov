"""Тесты задачи 05-11 «Медиана»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_11_median.py"


def test_median_odd():
    assert out_lines(run_script(TASK, "5 1 3\n")) == ["3"]


def test_median_even():
    assert out_lines(run_script(TASK, "4 1 3 2\n")) == ["2.5"]


def test_median_two_same():
    assert out_lines(run_script(TASK, "7 7\n")) == ["7.0"]


def test_median_single():
    assert out_lines(run_script(TASK, "9\n")) == ["9"]
