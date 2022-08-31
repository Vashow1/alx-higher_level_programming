#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    big_num = 0
    for key in a_dictionary:
        if a_dictionary[key] > big_num:
            biggest = key
            big_num = a_dictionary[key]
    return biggest
