#!/usr/bin/python3
"""Creates a python object from json file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        data = json.load(a_file)
    return (data)
