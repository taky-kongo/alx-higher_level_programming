#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix[i]) - 1 != j:
                print("{}".format(matrix[i][j]), end=" ")
            else:
                print("{}".format(matrix[i][j]))
