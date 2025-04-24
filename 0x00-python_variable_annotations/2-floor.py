#!/usr/bin/env python3
"""
This module provides a function that returns the floor of
a floating-point number.
It uses the math module to perform the operation and
demonstrates type annotations.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The greatest integer less than or equal to n.
    """

    return math.floor(n)
