#!/usr/bin/python3
"""Implementation of a function ``from_json_string(my_str)``"""
import json


def from_json_string(my_str):
    """a function that returns an object(python data structure)
    represented by a JSON string.
        Arg:
            my_str: the string represented by a json string.
        Return: returns an object of python data structure.
    """
    return json.loads(my_str)
