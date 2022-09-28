#!/usr/bin/python3
"""converts stringt to json rep"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    stringjson = json.dumps(my_obj)
    return (stringjson)
