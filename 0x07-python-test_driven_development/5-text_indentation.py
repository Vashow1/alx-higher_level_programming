#!/usr/bin/python3
"""Module with fn that formats the printing of text"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each
    of these characters: ., ? and :

    """
    if type(text) != str:
        raise TypeError("text must be a string")

    checkers = ['.', '?', ':']
    text = text.strip(" ")
    temp = 0
    for char in text:
        if char == ' ' and temp == 1:
            pass
        else:
            temp = 0
            print(char, end="")
            if char == '\n':
                temp = 1
        if char in checkers:
            print("\n\n", end="")
            temp = 1
