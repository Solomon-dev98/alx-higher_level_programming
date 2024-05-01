#!/usr/bin/python3
"""Implementation a class Student"""


class Student:
    """a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor method for the class with public instance
            attributes.
            Args:
                first_name: an attribute
                last_name: an attribute
                age: a public instance attribute.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A public method with attributes set to None that
            retrieves a dictionary represention of a Student obj.
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
