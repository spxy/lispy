"""Tests for Lispy."""

import pytest

from lispy import EOFError, ParenError, parse, tokenize


def test_tokenize() -> None:
    assert tokenize("(+ 1 2)") == ["(", "+", "1", "2", ")"]


def test_parse() -> None:
    assert parse("+") == "+"
    assert parse("foo") == "foo"
    assert parse("1") == 1
    assert parse("1.23") == 1.23
    assert parse("(+ 1 2)") == ["+", 1, 2]
    assert parse("(list (10 20 (+ 30 40)))") == ["list", [10, 20, ["+", 30, 40]]]


def test_parse_eof_error() -> None:
    with pytest.raises(EOFError) as excinfo:
        parse("(")
    with pytest.raises(EOFError) as excinfo:
        parse("(+ 1 2")
    with pytest.raises(EOFError) as excinfo:
        parse("(list (+ 1 2)")


def test_parse_paren_error() -> None:
    with pytest.raises(ParenError) as excinfo:
        parse(")")
    with pytest.raises(ParenError) as excinfo:
        parse("(+ 1 2))")
