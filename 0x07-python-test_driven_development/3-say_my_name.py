#!/usr/bin/python3
"""An implementation of a function ``say_my_name``"""


def say_my_name(first_name, last_name=""):
    """ a function that prints first name and last name.

        Args:
            first_name(str): the first name.
            last_name(str, optional): the last_name.

        Raises:
            TypeError: if the first name is not a string.
            TypeError: if the last name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
