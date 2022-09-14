#!/usr/bin/python3
"""Demonstrate validation"""


class Square:
    """A class representation of a square shape"""

    def __init__(self, size=0):
        """initializing the square"""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if (isinstance(value, int)):
            pass
        else:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""
        return (self.__size ** 2)
