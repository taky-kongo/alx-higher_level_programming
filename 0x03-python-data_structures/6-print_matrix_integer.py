#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix[i]) - 1 != j:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))
