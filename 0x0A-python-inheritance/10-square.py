#!/usr/bin/python3
"""Implelementation of a class Square"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from parent class Rectangle"""
    def __init__(self, size):
        """the constructor method for class Square.

            Args:
                size: a private field or attribute.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the Square"""
        return (self.__size * self.__size)
