#!/usr/bin/python3
"""Defines an integer addition function."""


def _add(x, y):
    add = int(x) + int(y) if isinstance(x, float)\
        or isinstance(y, float) else x + y
    return add


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first int.
        b: second int, default value is 98.

    Raises:
        TypeError: if a, b are neither int nor float.

    Returns:
        sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = _add(a, b)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
