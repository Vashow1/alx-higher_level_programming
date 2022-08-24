#!/usr/bin/python3
def print_last_digit(number):
    numStr = str(number)
    last_digit = int(numStr[-1])
    if last_digit >= 0 and last_digit <=9:
        print(last_digit, end='')
        return (last_digit)
    else:
        return None
