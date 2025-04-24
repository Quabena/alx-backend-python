#!/usr/bin/env python3
"""
This module defines a function that returns a list of tuples,
each containing an element and its length.
"""


from typing import List, Tuple, Iterable, TypeVar

T = TypeVar('T', bound=Iterable)


def element_length(lst: List[T]) -> List[Tuple[T, int]]:
    """
    Returns a list of tuples with elements and their lengths.

    Args:
        lst (List[T]): A list of iterable elements.

    Returns:
        List[Tuple[T, int]]: A list of tuples where each tuple contains
        an element from the list and its length.
    """

    return [(i, len(i)) for i in lst]
