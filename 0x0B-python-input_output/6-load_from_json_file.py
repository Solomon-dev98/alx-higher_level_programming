#!/usr/bin/python3
"""Implementation of a function ``def load_from_json_file(filename)"""
import json


def load_from_json_file(filename):
    """a function that creates an object from a "JSON file".

        Args:
            filename: the file where json object is created from.
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        return json.loads(data)
