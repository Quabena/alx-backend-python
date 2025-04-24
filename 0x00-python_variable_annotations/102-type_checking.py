#!/usr/bin/env python3
"""
This module defines a function that repeats elements in a list
a number of times (zoom effect).
"""

from typing import List, Any


def zoom_array(lst: List[Any], factor: int = 2) -> List[Any]:
    """
    Returns a new list where each element in the input list
    is repeated 'factor' number of times.

    Args:
        lst (List[Any]): The input list.
        factor (int): Number of times to repeat each element.

    Returns:
        List[Any]: The zoomed-in list.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)       # Valid: factor = 2 (default)
zoom_3x = zoom_array(array, 3)    # Fixed: now factor is an int

