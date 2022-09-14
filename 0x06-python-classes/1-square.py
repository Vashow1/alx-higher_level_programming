#!/usr/bin/python3
"""Demonstrate a private attribute"""


class Square:
    """A class representation of a square shape"""

    def __init__(self, size=None):
        """initializing the square"""
        self.__size = size
