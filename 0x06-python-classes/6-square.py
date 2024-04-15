#!/usr/bin/python3
"""a representation of a class square"""


class Square:
    """definition of a class square with size and positon attr"""
    def __init__(self, size=0, position=(0, 0)):
        """ an initialization of an instance of the class Square.
        Args:
            size(int, optional): the size of the square.
            position: a private instance attribute.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """" a getter method that retrives the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter method that is responsible for changing the value.
        Args:
            value: the value field.

        Raises:
            TypeError: size is not an integer.
            ValueError: size is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ the getter method that retrieves size"""
        return self.__position

    @position.setter
    def position(self, value):
        """the setter method that changes the value
        Args:
            value: the value size is set to.

        Raises:
            TypeError: position is not a tuple of 2 positive int.
        """
        if not (isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(item, int) for item in value) or
                not all(item >= 0 for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ a public instance method that prints in stdout
        the square with the ch #"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
