#!/usr/bin/python3
"""Implementation of a function that adds two integers"""


def add_integer(a, b=98):
    """
        function that adds two integers.

        Args:
            a(int or float): an argument to the function.
            b(int or float): an argument to the function.

        Raises:
            TypeError: a or b is not an integer.
    """
    if ((not isinstance(a, int) and not isinstance(b, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
