#!/usr/bin/python3
"""converts json rep to python obj"""


import json


def from_json_string(my_obj):
    """returns the an object (Python data structure) represented by a JSON string"""
    pythonobj = json.loads(my_obj)
    return (pythonobj)
