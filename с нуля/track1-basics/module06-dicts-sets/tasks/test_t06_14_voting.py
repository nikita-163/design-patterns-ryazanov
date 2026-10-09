"""Тесты задачи 06-14 «Голосование»."""
from pathlib import Path

from coursekit.runner import out_lines, run_script

TASK = Path(__file__).parent / "t06_14_voting.py"


def test_voting_winner():
    assert out_lines(
        run_script(TASK, "5\nборис\nанна\nборис\nанна\nанна\n")
    ) == ["анна 3"]


def test_voting_tie_alphabetical():
    assert out_lines(run_script(TASK, "4\nб\nа\nб\nа\n")) == ["а 2"]


def test_voting_single():
    assert out_lines(run_script(TASK, "1\nвика\n")) == ["вика 1"]
