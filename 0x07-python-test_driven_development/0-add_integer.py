#!/usr/bin/python3
"""Implementation of a function that adds two integers"""


def add_integer(a, b=98):
    """
        function that adds two integers.

        Args:
            a(int or float): the first number.
            b(int or float, optional): the second number. defaults to 98.

        Returns:
            int: the sum of a and b.
        Raises:
            TypeError: a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
