#!/usr/bin/python3
"""contains a function that writes json to file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
