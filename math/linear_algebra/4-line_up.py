#!/usr/bin/env python3
"""Write a function def add_arrays(arr1, arr2)
that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """add_arrays"""
    if len(arr1) == len(arr2):
        new_array = []
        for a, b in zip(arr1, arr2):
            new_array.append(a + b)
        return new_array
    return None
