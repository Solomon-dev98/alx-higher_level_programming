#!/usr/bin/python3
"""Implementation of a class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherits from another class BaseGeometry"""
    # The constructor
    def __init__(self, width, height):
        """ A constructor method that instantiates with width and height.

            Args:
                width: private data fiel to be validated to be an int.
                height: private data field to be validated to be an int.
        """
        # Validate width and height

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
