#!/usr/bin/python3
"""Contains function to append text to a file"""


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
    return (len(text))
