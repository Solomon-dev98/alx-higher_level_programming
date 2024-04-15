#!/usr/bin/python3

"""A square that defines a square based on 1-square.py"""


class Square:

    def __init__(self, size=0):
        """ An init method with a private instances attribute

        Args:
            size: initial value is 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
