#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc_len = 0

    argc_len = len(sys.argv) - 1
    if (argc_len == 0):
        print("0 arguments.")
    elif argc_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc_len))
        for i in range(argc_len):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
