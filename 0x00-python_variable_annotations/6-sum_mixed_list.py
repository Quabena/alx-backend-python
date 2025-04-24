#!/usr/bin/env python3
"""
This module defines a function to compute the sum of a list
containing both integers and floats using type annotations.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list
        containing int and float elements.

    Returns:
        float: The total sum of all the values in the list.
    """

    return sum(mxd_lst)
