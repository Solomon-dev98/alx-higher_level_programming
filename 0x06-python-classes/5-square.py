#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """A definition of a square"""
    def __init__(self, size=0):
        """ initialises an instance of the class Square.

        Args:
            size: The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """ the getter method that retrieves the size.

        Return: returns the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ a property that sets the value of the size.

        Args:
            value: the value field.

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
        """Return: returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
