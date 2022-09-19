#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """The class definition"""
    def __init__(self, width=0, height=0):
        """Initialise the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the recctangle and return it"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes the perimeter of the rectangle and return it"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))
    def __str__(self):
        output = ""
        for i in range(self.__height):
            for i in range(self.__width):
                output += "#"
            output += '\n'
        return (output)
