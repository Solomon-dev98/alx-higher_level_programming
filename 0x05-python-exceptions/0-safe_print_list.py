#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        length = 0

        if my_list:
            for i in range(x):
                print(my_list[i], end="")
                length += 1
    except IndexError:
        pass
    finally:
        print()
    return length
