#!/usr/bin/python3
"""Implementation of a function ``write_file(filename="", text="")``"""


def write_file(filename="", text=""):
    """a function that writes to a text file and returns
        the number of characters written.

        Args:
            filename: the file to be written to.
            text(str): the string to be written to the file.

        Return: returns the number of character written.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        num_char = file.write(text)
        return num_char
