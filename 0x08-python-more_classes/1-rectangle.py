#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """A class that defines a class for the shape rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute of the instance"""
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute of the instance"""
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
