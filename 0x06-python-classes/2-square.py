#!/usr/bin/python3

"""A square that defines a square based on 1-square.py"""


class Square:

    def __init__(self, size=0):
        """ An init method that initializes a the class Square.

        Args:
            size: initial value is 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0>
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
