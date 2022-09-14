#!/usr/bin/python3
"""Demonstrate validation"""


class Square:
    """A class representation of a square shape"""

    def __init__(self, size=0):
        """initializing the square"""
        self.__size = size
        if (isinstance(size, int)):
            pass
        else:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """Computes the area of the square"""
        return (self.__size ** 2)
