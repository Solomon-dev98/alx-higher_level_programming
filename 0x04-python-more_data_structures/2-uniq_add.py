#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_elements = set(my_list)

    sum_all = 0
    for element in uniq_elements:
        sum_all += element

    return sum_all
