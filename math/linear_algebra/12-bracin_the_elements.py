#!/usr/bin/env python3
"""Write a function def np_elementwise(mat1, mat2) that
performs element-wise addition, subtraction, multiplication, and division"""


def np_elementwise(mat1, mat2):
    """np_elementwise"""
    add = (mat1 + mat2)
    sub = (mat1 - mat2)
    mul = (mat1 * mat2)
    div = (mat1 / mat2)
    return add, sub, mul, div
