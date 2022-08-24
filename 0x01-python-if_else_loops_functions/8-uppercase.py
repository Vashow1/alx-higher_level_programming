#!/usr/bin/python3
def uppercase(str):
    for char in str:
        charIn = ord(char)
        if char >= 'a' and char <= 'z':
            charIn = charIn - 32
        print("{}".format(chr(charIn)), end='')
    print()
