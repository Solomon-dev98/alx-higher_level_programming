#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc_len = len(sys.argv) - 1

    add = 0

    for i in range(argc_len):
        add = add + int(sys.argv[i + 1])

    print(add)
