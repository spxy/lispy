"""Tests for Lispy."""

import pytest

from lis import UnclosedParenError, UnexpectedCloseParenError, parse, tokenize


def test_tokenize() -> None:
    assert tokenize("(+ 1 2)") == ["(", "+", "1", "2", ")"]


def test_parse() -> None:
    assert parse("+") == ["+"]
    assert parse("foo") == ["foo"]
    assert parse("1") == [1]
    assert parse("1.23") == [1.23]
    assert parse("(+ 1 2)") == [["+", 1, 2]]
    assert parse("(list (10 20 (+ 30 40)))") == [["list", [10, 20, ["+", 30, 40]]]]


def test_parse_eof_error() -> None:
    with pytest.raises(UnclosedParenError):
        parse("(")
    with pytest.raises(UnclosedParenError):
        parse("(+ 1 2")
    with pytest.raises(UnclosedParenError):
        parse("(list (+ 1 2)")


def test_parse_paren_error() -> None:
    with pytest.raises(UnexpectedCloseParenError):
        parse(")")
    with pytest.raises(UnexpectedCloseParenError):
        parse("(+ 1 2))")
