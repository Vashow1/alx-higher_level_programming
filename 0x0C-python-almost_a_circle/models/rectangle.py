#!/usr/bin/python3
"""This module contains the definition of the rectangle shape class"""
from models.base import Base


class Rectangle(Base):
    """Definition of the shape"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises the class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the value of the private attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the private attribute width"""
        self.__width = width

    @property
    def height(self):
        """returns the value of the private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the private attribute height"""
        self.__height = height

    @property
    def x(self):
        """returns the value of the private attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the private attribute x"""
        self.__x = x
    
    @property
    def y(self):
        """returns the value of the private attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the private attribute y"""
        self.__y = y
