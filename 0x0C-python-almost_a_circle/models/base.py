#!/usr/bin/python3
"""This module contains the definition of the class Base"""
import json
import csv


class Base:
    """Definition of the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as a_file:
            if list_objs is None:
                a_file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                a_file.write(Base.to_json_string(list_dict))
