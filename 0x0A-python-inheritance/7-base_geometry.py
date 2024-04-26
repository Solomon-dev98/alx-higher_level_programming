#!/usr/bin/python3
"""Implementation of a class BaseGeometry"""


class BaseGeometry:
    """a class with public instance method ``area``, ``integer_validator``."""

    def area(self):
        """A public instance method that raises an Exception when
            not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance that validates a value if it's an integer.

            Args:
                name(str): a string.
                value(int): the value to be validated.
            Raises:
                TypeError: value is not an integer.
                ValueError: value is less than or equal to 0.
        """
        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
