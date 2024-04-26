#!/usr/bin/python3
"""Implementation of a class BaseGeometry"""


class BaseGeometry:
    """a class with public instance ``area`` that raises an exception"""
    def area(self):
        """a public instance method"""
        raise NotImplementedError("area() is not implemented")
