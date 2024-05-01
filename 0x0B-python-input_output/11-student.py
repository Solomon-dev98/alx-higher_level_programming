#!/usr/bin/python3
"""Implementation of a class Student"""


class Student:
    """A class that defines a student with public instance attributes."""

    def __init__(self, first_name, last_name, age):
        """the constructor method that instantiates an instance
            of the class.
            Args:
                first_name: a public attribute.
                last_name: a public attribute
                age:    a public attribute.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A public method that retrieves a dict repr of Student.
        """
        if (isinstance(attrs, list)
           and all(type(ele) is str for ele in attrs)):
            attributes = {}
            for attribute_name in attrs:
                if (hasattr(self, attribute_name)):
                    attribute_value = getattr(self, attribute_name)
                    attributes[attribute_name] = attribute_value
            return attributes
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """A public method that replaces all attributes of
        the student instance.
        Args:
            json(dict): a public instance attribute.
        """
        for keys, values in json.items():
            setattr(self, keys, values)
