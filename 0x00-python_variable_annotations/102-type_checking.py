#!/usr/bin/env python3
"""
This module defines a function that returns a new list
by repeating each element of a tuple a specified number of times.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a zoomed-in list where each element of the input tuple
    is repeated 'factor' times.

    Args:
        lst (Tuple): The input tuple of elements.
        factor (int): Number of repetitions for each element.

    Returns:
        List: The zoomed-in list.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

