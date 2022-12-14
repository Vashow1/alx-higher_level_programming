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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already
        set based on **dictionary
        note size, width and length must be > 0 hence the dummy values used

        """
        if dictionary != {} and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as a_file:
                list_dict = Base.from_json_string(a_file.read())
                return [cls.create(**dictionary) for dictionary in list_dict]
        except IOError:
            return []
