#!/usr/bin/python3
"""Implementation of a function ``is_a_kind_of_class(obj, a_class)``"""


def is_kind_of_class(obj, a_class):
    """A function that checks if an object is an instance of or class \
            the object inherited from the specified class.

        Args:
            obj: the object to check for its class
            a_class: the specified class.

        Return:
            bool: True or false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
