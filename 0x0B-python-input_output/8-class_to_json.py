#!/usr/bin/python3
"""Implementation of a function ``class_to_json(obj)``"""


def class_to_json(obj):
    """a function that returns a dictionary description with
        simple data structure for JSON serialization of obj.

        Args:
            obj: An instance of a class.
        Return: returns a dict description.
    """
    return obj.__dict__
