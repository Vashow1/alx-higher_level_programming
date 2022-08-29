#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x_list = [0, 0]
    mix_tuple = (tuple_a, tuple_b)
    for tup in mix_tuple:
        i = 0
        for element in tup:
            if i > 1:
                break
            x_list[i] += element
            i += 1
    new_tuple = (x_list[0], x_list[1])
    return new_tuple
