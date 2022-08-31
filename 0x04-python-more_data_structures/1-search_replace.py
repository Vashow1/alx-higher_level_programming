#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for integer in my_list:
        if integer == search:
            integer = replace
        new_list.append(integer)
    return new_list
