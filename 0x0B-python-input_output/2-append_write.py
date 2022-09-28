#!/usr/bin/python3
"""Contains function to append text to a file"""


def append_write(filename="", text=""):
    """Opens filename and appends text to it"""

    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
    return (len(text))
