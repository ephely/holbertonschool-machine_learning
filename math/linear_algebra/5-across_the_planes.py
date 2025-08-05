#!/usr/bin/env python3
"""Write a function def add_matrices2D(mat1, mat2)
that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """def add_matrices2D"""
    new_matrix = []
    if len(mat1) == len(mat2):
        for row1, row2 in zip(mat1, mat2):
            if len(row1) != len(row2):
                return None
            new_row = [a + b for a, b in zip(row1, row2)]
            new_matrix.append(new_row)
    return new_matrix
