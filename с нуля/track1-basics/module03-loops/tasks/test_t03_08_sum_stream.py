"""Тесты задачи 03-08 «Сумма потока»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t03_08_sum_stream.py"


def test_sum_stream_4():
    assert out_lines(run_script(TASK, "4\n1\n2\n3\n4\n")) == ["10"]


def test_sum_stream_5():
    assert out_lines(run_script(TASK, "5\n1\n2\n3\n4\n5\n")) == ["15"]


def test_sum_stream_negatives():
    assert out_lines(run_script(TASK, "3\n-10\n5\n-1\n")) == ["-6"]
