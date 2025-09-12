Susam's Lispy
=============

This project contains implementations of Scheme-like interpreters
based on the 2018 version of Peter Norvig's Lispy interpreters.
Neither implementation is an exact reproduction of Norvig's work.  In
fact, both the languages and the interpreters implemented here differ
quite a bit from his.  Nevertheless, they are clearly inspired by
Lispy, and I would like to thank Peter Norvig for creating the
original Lispy implementations.

The original implementations by Norvig are available under the MIT
licence in his [pytudes][] project.  Copies of his implementations
from 2018 are preserved under the [norvig/][] subdirectory of this
project.

[pytudes]: https://github.com/norvig/pytudes
[norvig/]: norvig/


Contents
--------

* [Simple Lispy (lis.py)](#simple-lispy-lis.py)
  * [Norvig's Simple Lispy](#norvigs-simple-lispy)
  * [Susam's Simple Lispy](#susams-simple-lispy)


Simple Lispy (lis.py)
---------------------


## Norvig's Simple Lispy

The first Lispy interpreter implemented by Norvig was [lis.py][].
Norvig introduced this interpreter in this well known article: [(How
to Write a (Lisp) Interpreter (in Python))][norvig-lispy-html].
However, the version linked in that article is outdated (as of July
2025).  A more recent version, from 2018, is available in Norvig's
[pytudes][] project, and is also archived in this project at
[norvig/lis.py][].  The [lis.py][] program implemented in this project
is based on Norvig's 2018 version.

In this project, Norvig's Lispy REPL can be executed with Python 3.3
or a later version, as follows:

```sh
python3 -c "from norvig.lis import repl; repl()"
```

[lis.py]: lis.py
[norvig/lis.py]: norvig/lis.py
[norvig-lispy-html]: https://norvig.com/lispy.html


## Susam's Simple Lispy

As mentioned earlier, the implementation here differs quite a bit from
Norvig's implementation.  In this project, my Lisp REPL can be
executed with Python 3.11 or a later version, as follows:

```sh
python3 lis.py
```

The list below presents a non-exhaustive list of differences between
my implementation of Lispy and Norvig's implemnetation of Lispy:

 1. My Lispy comes with a suite of unit tests.  The unit tests are
    available at [test/test_lispy.py](test/test_lispy.py).

 2. My Lispy exits gracefully on reaching the end of the standard input stream:

    ```
    > ^D
    $
    ```

    Norvig's Lispy encounters `EOFError` after reaching the end of the
    standard input stream.

    ```
    lis.py> ^D
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/Users/susam/git/lispy/norvig/lis.py", line 97, in repl
        val = eval(parse(input(prompt)))
                         ^^^^^^^^^^^^^
    EOFError
    ```

 3. My Lispy comes with `readline` support. So the usual GNU Readline
    or BSD Editline key sequences may be used.  For example, the
    <kbd>↑</kbd> key (the up arrow key) or
    <kbd>ctrl</kbd>+<kbd>p</kbd> brings back the previous input.

    ```
    > (+ 1 2)
    3
    > (+ 1 2)
    ```

    Norvig's Lispy does not have `readline` support.

    ```
    lis.py> (+ 1 2)
    3
    lis.py> ^[[A
    ```

 4. My Lispy explicitly detects incomplete top-level forms and waits
    for more input:

    ```
    > (+ 1 2
    ?
    ```

    The `?` prompt indicates that there is an incomplete top-level
    form.  The top-level form may then be completed and evaluated as
    shown below:

    ```
    > (+ 1 2
    ?    3 4)
    10
    ```

    Norvig's Lispy produces the following error while reading this program:

    ```
    lis.py> (+ 1 2
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/Users/susam/git/lispy/norvig/lis.py", line 97, in repl
        val = eval(parse(input(prompt)))
                   ^^^^^^^^^^^^^^^^^^^^
      File "/Users/susam/git/lispy/norvig/lis.py", line 62, in parse
        return read_from_tokens(tokenize(program))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/Users/susam/git/lispy/norvig/lis.py", line 75, in read_from_tokens
        while tokens[0] != ')':
              ~~~~~~^^^
    IndexError: list index out of range
    ```

 4. My Lispy can evaluate multiple top-level forms entered in a single
    line of input:

    ```
    > (+ 1 2)(+ 3 4)(+ 5 6)
    3
    7
    11
    ```

    Norvig's Lispy evaluates only the first top-level form when
    multiple forms are entered in a single line of input:

    ```lisp
    lis.py> (+ 1 2)(+ 3 4)(+ 5 6)
    3
    ```

 5. When there are multiple complete top-level forms followed by an
    incomplete top-level-form, My Lispy evaluates all the top-level
    forms and waits for more input as shown below:

    ```
    > (+ 1 2)(+ 3 4)(+
    3
    7
    ?
    ```

    The trailing incomplete form may then be completed and evaluated as follows:

    ```
    > (+ 1 2)(+ 3 4)(+
    3
    7
    ? 5 6)
    11
    ```

    Since Norvig's Lispy evaluates only the first top-level form, all
    subsequent top-level forms, including the incomplete one, are
    ignored:

    ```
    lis.py> (+ 1 2)(+ 3 4)(+
    3
    ```

 6. For various arithmetic functions, My Lispy accepts arbitrary
    number of arguments:

    ```
    > (+)
    0
    > (+ 1)
    1
    > (+ 1 2)
    3
    > (+ 1 2 3)
    6
    > (-)
    0
    > (- 10)
    -10
    > (- 10 1)
    9
    > (- 10 1 2)
    7
    ```

    Norvig's Lispy accepts exactly two arguments instead:

    ```
    lis.py> (+)
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/Users/susam/git/lispy/norvig/lis.py", line 97, in repl
        val = eval(parse(input(prompt)))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/Users/susam/git/lispy/norvig/lis.py", line 132, in eval
        return proc(*args)
               ^^^^^^^^^^^
    TypeError: add expected 2 arguments, got 0
    make: *** [nlis] Error 1
    ```

<!-- TODO: readline -->
