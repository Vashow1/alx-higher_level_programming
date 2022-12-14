#!/usr/bin/python3
"""This modules contains a fn that adds"""


def add_integer(a, b=98):
    """This function adds 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
