#!/usr/bin/python3
"""Opens and writes text to a file"""

def write_file(filename="", text=""):
    """Opens filename and writes text into it"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
    return (len(text))
