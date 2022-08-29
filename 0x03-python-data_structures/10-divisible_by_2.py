#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    conditions = my_list.copy()
    i = 0
    for item in my_list:
        if (item % 2) == 0:
            conditions[i] = True
        else:
            conditions[i] = False
        i += 1
    return conditions
