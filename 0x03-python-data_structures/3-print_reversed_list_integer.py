#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = 1
    for i in my_list:
        print(f"{my_list[-idx]}")
        idx += 1
