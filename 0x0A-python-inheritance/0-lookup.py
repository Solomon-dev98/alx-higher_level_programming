#!/usr/bin/python3
"""Implementation of function ``lookup(obj)``"""


def lookup(obj):
    """a function that returns a list of available attributes and methods /
        of an object.

    Args:
        obj: an object containing methods and attributes.

    Return: returns a list of attributs and methods.
    """

    return (dir(obj))
