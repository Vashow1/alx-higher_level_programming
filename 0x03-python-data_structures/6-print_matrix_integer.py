#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrice in matrix:
        i = 0
        for integer in matrice:
            length = len(matrice) - 1
            print("{:d}".format(integer), end='')
            if i < length:
                print(" ", end='')
            i += 1
        print()
