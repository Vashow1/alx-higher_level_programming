#!/usr/bin/python3
"""Defining a function that returns a list"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return (dir(obj))
