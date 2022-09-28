#!/usr/bin/python3
"""Class to json"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    jsonstr = obj.__dict__
    return jsonstr
