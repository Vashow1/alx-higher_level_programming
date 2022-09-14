#!/usr/bin/python3
"""Demonstrate validation"""


class Square:
    """A class representation of a square shape"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position attribute of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Defining the position attribute of the square"""
        if (isinstance(value, tuple)) and (len(value) == 2) and \
                (value[0] >= 0) and (value[1] >= 0):
            pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """a method that creates a square out of pound signs"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print('#', end="")

                print()
        else:
            print()
