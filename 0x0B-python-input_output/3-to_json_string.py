#!/usr/bin/python3
import json
"""Implementation of a function ``def to_json_striing(my_obj)``"""


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object(string).
    Args:
        my_obj: the string.
        Return: returns the JSON representation of the string>
    """
    return json.dumps(my_obj)
