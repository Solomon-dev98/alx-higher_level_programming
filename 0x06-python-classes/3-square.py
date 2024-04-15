#!/usr/bin/python3
""" writes a  class square that defines a square based on 2-square.py"""


class Square:
    """ Definiton of a class square"""

    def __init__(self, size=0):
        """ initializes a square instance with a size.

        Args:
            size(int, optional): the of the square. defaults to 0.

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

    def area(self):
        """ calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
