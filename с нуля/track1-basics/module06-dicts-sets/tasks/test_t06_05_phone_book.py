"""Тесты задачи 06-05 «Телефонная книга»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_05_phone_book.py"


def test_phone_found():
    assert out_lines(
        run_script(TASK, "2\nанна 111-22-33\nборис 555-66-77\nанна\n")
    ) == ["111-22-33"]


def test_phone_second():
    assert out_lines(
        run_script(TASK, "2\nанна 111\nборис 222\nборис\n")
    ) == ["222"]


def test_phone_missing():
    assert out_lines(
        run_script(TASK, "1\nанна 111\nвика\n")
    ) == ["не найдено"]
