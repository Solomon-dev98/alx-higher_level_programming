#!/usr/bin/python3
"""Implementation of a class ``Student``"""


class Student:
    """A class student that defines a student with attributes"""

    def __init__(self, first_name, last_name, age):
        """The constructor method with attributes.
            Args:
                first_name: a public instance attr.
                last_name: a public instance attr.
                age: a public instance attr.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ a public method  that retrieves a dictionary repr
            of a student instance."""
        return self.__dict__
