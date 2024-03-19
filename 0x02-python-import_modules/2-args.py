#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv_len = 0

    argv_len = len(sys.argv) - 1
    if (argv_len == 0):
        print("0 arguments.")
    else:
        print("{} arguments:".format(argv_len))
        for i in range(argv_len):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
