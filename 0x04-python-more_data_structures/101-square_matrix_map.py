#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x ** 2, matrix[0])), list(map(lambda x: x ** 2, matrix[1])), list(map(lambda x: x ** 2, matrix[2]))]
