#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers"""
    for row in matrix:
        for x in row:
            print("{:d}".format(x), end=" " if x != row[-1] else "")
            print()
