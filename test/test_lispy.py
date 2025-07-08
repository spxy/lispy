"""Tests for Lispy."""

from lispy import tokenize


def test_tokenize() -> None:
    assert tokenize("(+ 1 2)") == ["(", "+", "1", "2", ")"]
