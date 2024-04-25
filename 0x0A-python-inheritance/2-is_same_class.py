#!/usr/bin/python3
"""Implementation of a function ``is_same_class``"""


def is_same_class(obj, a_class):
    """a function that checks if the object is exactly an instance \
        of the specified class or otherwise.

        Args:
            obj: the object.
            a_class: the specified class

        Return:
            returns True or False if object is an instance \
                    of a specified class."""
    return type(obj) is a_class
