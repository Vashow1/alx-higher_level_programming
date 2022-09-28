#!/usr/bin/python3
"""Creates a function that prints contents of a file"""


def read_file(filename=""):
    """Opens a file and reads into it"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
