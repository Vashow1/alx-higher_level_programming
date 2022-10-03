#!/usr/bin/python3
"""This module contains the definition of the rectangle shape class"""
from models.base import Base


class Rectangle(Base):
    """Definition of the shape"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the value of the private attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the private attribute width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """returns the value of the private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the private attribute height"""
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """returns the value of the private attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the private attribute x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns the value of the private attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the private attribute y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Computes the area to a rectangle instance"""
        return (self.height * self.width)

    def display(self):
        """a method that creates a rectangle out of pound signs"""
        if self.width > 0 and self.height > 0:
            if self.y > 0:
                for ind in range(self.y):
                    print()
            for i in range(self.height):
                if self.x > 0:
                    for ind in range(self.x):
                        print(' ', end="")
                for i in range(self.width):
                    print('#', end="")
                print()
        else:
            print()

    def __str__(self):
        """The magic method that defines behavior on printing of class"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")

    def update(self, *args):
        """
        Updates the values of rectangle
        The index and iteration provides for a way to
        ensure that there is a value at the requested args
        index
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
