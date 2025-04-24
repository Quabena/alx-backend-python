#!/usr/bin/env python3
"""
This module provides a function that sums a list of
floating-point numbers.
It demonstrates the use of type annotations for list
parameters and return types.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all elements in the list.
    """

    return sum(input_list)
