#!/usr/bin/python3

# import the add function from the add_0 module
from add_0 import add


def main():
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))


# check if the script is run directly
if __name__ == "__main__":
    main()
