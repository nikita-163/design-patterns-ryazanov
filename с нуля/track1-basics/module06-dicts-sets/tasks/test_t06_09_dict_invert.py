"""Тесты задачи 06-09 «Обратный словарь»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_09_dict_invert.py"


def test_invert_numbers():
    assert out_lines(
        run_script(TASK, "3\none один\ntwo два\nthree три\n")
    ) == ["два: two", "один: one", "три: three"]


def test_invert_single():
    assert out_lines(run_script(TASK, "1\ncat кот\n")) == ["кот: cat"]


def test_invert_overwrite():
    # если русское слово повторяется, остаётся последнее английское
    assert out_lines(
        run_script(TASK, "2\ncat кот\ndog кот\n")
    ) == ["кот: dog"]
