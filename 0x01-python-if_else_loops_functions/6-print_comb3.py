#!/usr/bin/python3
for i in range(1, 90):
    if i != 89:
        if i / 10 <= 9:
            if i % 10 <= 9:
                if i / 10 < i % 10:
                    print("{:02d}, ".format(i), end="")
    elif i == 89:
        print("{:02d}".format(i))
