#!/usr/bin/python3
"""This module contains a fn to print a square"""


def print_square(size):
    """prints a square with the character #"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for ind in range(size):
        for ind in range(size):
            print("#", end="")
        print()
