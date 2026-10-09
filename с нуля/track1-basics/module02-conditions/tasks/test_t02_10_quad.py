"""Тесты задачи 02-10 «Корни квадратного уравнения»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t02_10_quad.py"


def test_two_roots():
    assert out_lines(run_script(TASK, "1\n-3\n2\n")) == ["два корня: 1.0 2.0"]


def test_two_roots_fractional():
    assert out_lines(run_script(TASK, "2\n5\n-3\n")) == ["два корня: -3.0 0.5"]


def test_one_root():
    assert out_lines(run_script(TASK, "1\n2\n1\n")) == ["один корень: -1.0"]


def test_no_roots():
    assert out_lines(run_script(TASK, "1\n0\n1\n")) == ["нет корней"]
