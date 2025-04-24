#!/usr/bin/env python3
"""
This module provides a function that converts a key and a
numeric value into a tuple containing the key and the
square of the value.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a numeric value.

    Args:
        k (str): The key to be used as the first element of the tuple.
        v (Union[int, float]): A numeric value (int or float).

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`,
        and the second element is the square of `v` as a float.
    """

    return (k, float(v ** 2))
