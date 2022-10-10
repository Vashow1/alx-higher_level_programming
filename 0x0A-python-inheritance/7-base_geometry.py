#!/usr/bin/python3
"""Module defines the class base_geometry"""


class BaseGeometry:
    """Preliminary declaration of class"""

    def area(self):
        """Area of the base geometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value:
        - assume name is always a string
        - if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        - if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0

        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
