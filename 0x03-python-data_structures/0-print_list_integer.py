#!/usr/bin/python3

""" a function that prints all integers of a list """


def print_list_integer(my_list=[]):

    length = len(my_list)

    for i in range(length):
        print("{:d}".format(my_list[i]))
