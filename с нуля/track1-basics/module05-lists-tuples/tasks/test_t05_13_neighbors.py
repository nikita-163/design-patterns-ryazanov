"""Тесты задачи 05-13 «Соседние равные»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t05_13_neighbors.py"


def test_neighbors_true():
    assert out_lines(run_script(TASK, "1 2 2 3\n")) == ["True"]


def test_neighbors_false():
    assert out_lines(run_script(TASK, "1 2 3\n")) == ["False"]


def test_neighbors_single():
    assert out_lines(run_script(TASK, "5\n")) == ["False"]
