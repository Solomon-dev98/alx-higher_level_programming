#!/usr/bin/python3
"""Implementation of a function ``read_file(filename="")``"""


def read_file(filename=""):
    """a function that reads a text file and prints it to stdout

        Args:
            filename: the file to be read.
    """

    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read()
        print(data, end='')
