#!/usr/bin/python3

""" definition of a class square"""


class Square:
    """ a class square that defines a square"""
    def __init__(self, size):
        """ the __init__ method initialises an instance of the class Square.

        Args:
            size: a private instance attribute with no type/value verification.
        """
        self.__size = size
