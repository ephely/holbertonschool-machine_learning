#!/usr/bin/env python3
"""Write a function def cat_matrices2D(mat1, mat2, axis=0)
that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """cat_matrices2D"""
    new_mat = []
    if axis == 0:
        if all(len(row) != len(mat1[0]) for row in mat1 + mat2):
            return None
        new_mat = mat1 + mat2
        return new_mat
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        for row1, row2 in zip(mat1, mat2):
            new_row = row1 + row2
            new_mat.append(new_row)
        return new_mat
    else:
        return None
        