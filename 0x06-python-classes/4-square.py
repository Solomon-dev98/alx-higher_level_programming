#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Representation of a square"""
    def __init__(self, size=0):
        """ initialises an instance of the class Square.

        Args:
            size(int, optional): the size of the square. defaults to 0.

        Raises:
            TypeError: size is not an integer.
            ValueError: size is less than 0.
        """

        self.__size = size

    @property
    def size(self):

        """ retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):

        """ A property setter.

        Args:
            value: a field to the size setter property.

        Raises:
            TypeError: size is not an integer.
            ValueError: size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
