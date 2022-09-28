#!/usr/bin/python3
"""Script containing a class that defines a student"""


class Student:
    """Definition of the class"""

    def __init__(self, first_name, last_name, age):
        """Initialises the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the json rep of the instance"""
        if attrs is None:
            return (self.__dict__)
        attrs2 = {x: self.__dict__[x] for x in attrs if x in self.__dict__}
        return (attrs2)
