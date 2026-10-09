"""Тесты задачи 03-07 «Максимум в потоке»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_07_max_stream.py"


def test_max_stream_5():
    assert out_lines(run_script(TASK, "5\n3\n9\n1\n7\n5\n")) == ["9"]


def test_max_stream_negative():
    assert out_lines(run_script(TASK, "3\n-5\n-2\n-10\n")) == ["-2"]


def test_max_stream_single():
    assert out_lines(run_script(TASK, "1\n42\n")) == ["42"]
