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
