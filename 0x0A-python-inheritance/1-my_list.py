#!/usr/bin/python3
""" Implemenation of a class ``MyList``"""


class MyList(list):
    """a class that inherits from a list a public instance method.

        Args:
            list: the parent/base class.
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
