#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            result = 0 
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            division.append(result)
    return division
