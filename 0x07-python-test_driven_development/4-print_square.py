#!/usr/bin/python3
"""Implementation of a function ``print_square``"""


def print_square(size):
    """a function that prints a square with th character #

        Args:
            size(int): the size length of the square.
        Raises:
            TypeError: size is not an integer.
            ValueError: size is less than 0.
            TypeError: size is a float and less than 0.
    """
    # check if size is not integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # check if size is a float and less than 0.
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # print the square
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()  # Move to the next line after printing each row
