#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Definition of the class MyList"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
