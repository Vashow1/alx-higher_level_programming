#!/usr/bin/python3
"""This module contains a fn capable of dividing matrices"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    if matrix == None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    end = len(matrix)
    index = 0
    divided = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lst in matrix:

        if type(lst) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        length = len(lst)
        if index != (end - 1):
            if length != len(matrix[index + 1]):
                    raise TypeError("Each row of the matrix must have the same size")

        innerDivided = []
        for elem in lst:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = elem / div
            innerDivided.append(round(result, 2))
        
        divided.append(innerDivided)
        index += 1

    return divided
