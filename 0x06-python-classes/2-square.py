#!/usr/bin/python3
# 2-square.py
"""define a class Square that defines a square based on 1-square.py"""


class Square:
    """ Definition of a class Square"""

    def __init__(self, size=0):
        """ An init method that initializes a class Square.

        Args:
            size(int): The size of the square. .

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
