#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """The class definition"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialise the rectangle"""
        Rectangle.number_of_instances += 1
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
        """Defines what prints when str() method is called"""
        output = ""
        if self.__height == 0 or self.__width == 0:
            return output
        for i in range(self.__height):
            for i in range(self.__width):
                output += str(self.print_symbol)
            output += '\n'
        output = output[:-1]
        return (output)

    def __repr__(self):
        """String representation of the rectangle/eval"""
        output = "Rectangle(" + str(self.__width)
        output += ", " + str(self.__height) + ")"
        return (output)

    def __del__(self):
        """Destroying an instance of the class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
