#!/usr/bin/python3
"""Implementation of a function 'text_indentation(text)'"""


def text_indentation(text):
    """
        A function that prints a text 2 lines after characters: '. , ? and :'.
        Args:
            text(str): The text to be printed.
        Raises:
            TypeError: text is not a string.
    """
    # check if text is not a string.
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # print the text

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
