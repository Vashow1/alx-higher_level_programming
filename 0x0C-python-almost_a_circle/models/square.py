#!/usr/bin/python3
"""This module contains the class for the shape square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the shape Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises a square inheriting its from the Rectangle class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the size of the square"""
        self.width = size
        self.height = size

    def __str__(self):
        """Defines the behaviour on print(<square instance>)"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """
        Updates the values of the square
        similar to the one of the parent class but with
        one less value since width == height

        """
        if args != 0 and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg

                index += 1

        elif kwargs != 0 and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                if key == "size":
                    self.size = value

                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y,
                }
