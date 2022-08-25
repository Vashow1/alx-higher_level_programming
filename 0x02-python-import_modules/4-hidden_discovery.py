#!/usr/bin/python3
import hidden_4
surprises = dir(hidden_4)
for surprise in surprises:
    if surprise[0] != '_' and surprise[1] != '_':
        print(surprise)

