#!/usr/bin/python3

def best_score(a_dictionary):
    biggest_score = ""
    initial_value = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > initial_value:
                biggest_score = key
                initial_value = value

    else:
        return (None)

    return biggest_score
