#!/usr/bin/python3
"""Implementation of a function ``save_to_json_file``"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an object to a text, using json repr

        Args:
            my_obj: the object to write to a text file.
            filename: the file the text is to be written to.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
