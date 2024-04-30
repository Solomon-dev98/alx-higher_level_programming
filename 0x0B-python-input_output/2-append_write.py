#!/usr/bin/python3
"""Implementation of a function ``append_write(filename="", text="")``"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file
        and returns the number of characters.
        Args:
            filename: the file the string of text of text is appended.
            text: the string of text to be appended.
        Return: returns the number of charactes added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars_added = file.write(text)
        return chars_added
