Susam's Lispy
=============

This is an implementation of a Scheme-like interpreter based on Peter
Norvig's [Lispy][norvig-lispy].  This is not an exact reimplementation
of Norvig's Lispy.  In fact, the language here, as well as the
interpreted implemented here differ quite a bit from Norvig's
implementation.  Despite the differences, the interpreter here is
clearly inspired by Norvig's Lispy, so a big thanks to Peter Norvig
for writing the original Lispy implementation.

[norvig-lispy]: https://norvig.com/lispy.html


Differences
-----------

This section presents a non-exhaustive list of differences between my
implementation of Lispy (henceforth known as Susam's Lispy) and
Norvig's implemnetation of Lispy.  This section uses the version of
Norvig's Lispy as accessed on 20 Apr 2025.  A copy of it can be found
on the Wayback Machine here: [lis.py][wm-lispy].

[wm-lispy]: https://web.archive.org/web/20250420061514/https://norvig.com/lis.py

 1. The Lispy implementation here comes with a suite of unit tests.
    The unit test are available at [test/test_lispy.py](test/test_lispy.py).
    These unit tests (especially, the `test_eval_*` functions) provide
    an overview of the Lispy language.

 2. The Lispy implementation here explicitly detects unbalanced
    parentheses and raises a custom error.  For example consider the
    following Lispy program:

    ```lisp
    (+ 1 2
    ```

    Norvig's Lispy produces the following error while reading this program:

    ```
    Traceback (most recent call last):
      File "/Users/susam/git/lispy/lis.py", line 146, in <module>
        print(eval(parse("(+ 1 2")))
      File "/Users/susam/git/lispy/lis.py", line 19, in parse
        return read_from_tokens(tokenize(program))
      File "/Users/susam/git/lispy/lis.py", line 32, in read_from_tokens
        while tokens[0] != ')':
    IndexError: list index out of range
    ```

    Susam's Lispy produces the following error instead:

    ```
    ERROR: Unexpected end of input
    ```
