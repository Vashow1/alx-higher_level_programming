#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final_list = []
    for matrice in matrix:
        squares = list(map(lambda x: x ** 2, matrice))
        final_list.append(squares)
    return final_list
