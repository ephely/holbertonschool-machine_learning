#!/usr/bin/env python3
"""Write a function def mat_mul(mat1, mat2)
that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """mat_mul"""
    result_matrix = []
    if len(mat1[0]) != len(mat2):
        return None
    for row in mat1:
        new_row = []
        for j in range(len(mat2[0])):
            col = [row2[j] for row2 in mat2]
            result = sum(a * b for a, b in zip(row, col))
            new_row.append(result)
        result_matrix.append(new_row)
    return result_matrix
