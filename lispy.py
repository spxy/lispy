#!/usr/bin/env python3

# Copyright (c) 2025 Susam Pal
#
# You can use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of it, under the terms of the MIT License.  See
# COPYRIGHT.md for complete details.
#
# This software is provided "AS IS", WITHOUT WARRANTY OF ANY KIND,
# express or implied.  See COPYRIGHT.md for complete details.


"""Lispy - A Scheme-like interpreter implementation in Python.

This implementation is based on Peter Norvig's Lispy
<https://www.norvig.com/lispy.html>.  However, this is not an exact
reimplementation of Norvig's Lispy.  In fact, the language here, the
REPL, as well as the interpreter implemented here differ quite a bit
from Norvig's implementation.
"""

import functools
import operator
import pathlib
import re
import readline
from typing import Any, TypeAlias

HISTORY_FILE: pathlib.Path = pathlib.Path("~/.repl_history").expanduser()


Symbol: TypeAlias = str
Number: TypeAlias = int | float
Atom: TypeAlias = Symbol | Number
List: TypeAlias = list
Expr: TypeAlias = List | Atom
Env: TypeAlias = dict


def tokenize(program: str) -> list[str]:
    """Tokenize the given program into a list of tokens."""
    return re.findall(r"\(|\)|[^\s()]+", program)


def parse(program: str) -> Expr:
    """Parse the given progrma into a syntax tree."""
    expr, _ = parse_pos(tokenize(program))
    return expr


def parse_pos(tokens: list[str], pos: int = 0) -> tuple[Expr, int]:
    """Parse the list of tokens into a expression."""
    if tokens[pos] == "(":
        pos += 1
        expr = []
        while pos < len(tokens) and tokens[pos] != ")":
            sub_expr, pos = parse_pos(tokens, pos)
            expr.append(sub_expr)
        if pos == len(tokens):  # Reached EOF without encountering ')'.
            raise AbruptEndError
        return expr, pos + 1
    if tokens[pos] == ")":  # Unmatched parenthesis remains.
        raise CloseParenError()
    return atom(tokens[pos]), pos + 1


def atom(token: str) -> Atom:
    """Convert the given token into a Lisp atom."""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)


top_level_env: dict[str, Any] = {
    "+": lambda *args: functools.reduce(operator.add, args),
    "-": lambda *args: functools.reduce(operator.sub, args),
    "*": lambda *args: functools.reduce(operator.mul, args),
    "/": lambda *args: functools.reduce(operator.truediv, args),
    "<": lambda *args: all(x > y for x, y in zip(args, args[1:], strict=False)),
    ">": lambda *args: all(x < y for x, y in zip(args, args[1:], strict=False)),
    "<=": lambda *args: all(x <= y for x, y in zip(args, args[1:], strict=False)),
    ">=": lambda *args: all(x >= y for x, y in zip(args, args[1:], strict=False)),
    "length": len,
    "begin": lambda *x: x[-1],
    "list": lambda *x: list(x),
}


def evaluate(expr: str, env: Env = top_level_env) -> int | float:
    """Evaluate the given expression with the given environment."""
    if isinstance(expr, str):
        return env[expr]
    if isinstance(expr, (int, float)):
        return expr
    if expr[0] == "if":
        test_form, then_form, else_form = expr[1:]
        if evaluate(test_form, env):
            return evaluate(then_form, env)
        return evaluate(else_form, env)
    if expr[0] == "define":
        symbol, exp = expr[1:]
        env[symbol] = evaluate(exp, env)
        return env[symbol]

    proc = evaluate(expr[0], env)
    args = [evaluate(arg, env) for arg in expr[1:]]
    return proc(*args)


def repl() -> None:
    """Run Lispy REPL."""
    if pathlib.Path(HISTORY_FILE).exists():
        readline.read_history_file(HISTORY_FILE)
    while True:
        try:
            line = input("> ")
            readline.write_history_file(HISTORY_FILE)
            val = evaluate(parse(line))
            if val is not None:
                print(string(val))
        except EOFError:
            break
        except Exception as e:  # noqa: BLE001 blind-except
            print("ERROR:", e)


def string(expr: str) -> str:
    """Create a string representation of the given expression."""
    if isinstance(expr, list):
        return "(" + " ".join(string(x) for x in expr) + ")"
    return str(expr)


class AbruptEndError(Exception):
    """Unexpected EOF error."""

    def __init__(self):
        super().__init__("Unexpected end of input")


class CloseParenError(Exception):
    """Unexpected EOF error."""

    def __init__(self):
        super().__init__("Unexpected close parenthesis")


class ParseError(Exception):
    """Parse error."""


if __name__ == "__main__":
    repl()
