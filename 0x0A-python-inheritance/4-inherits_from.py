#!/usr/bin/python3
"""Implementation of a function ``inherits_from(obj, a_class)``"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance \
            of a class that inherited directly or indirectly from a \
            specified class, otherwise false.
        Args:
            obj: The object to be checked.
            a_class: the class to check against.
        Return:
            bool: True or false.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
