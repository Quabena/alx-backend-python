#!/usr/bin/env python3
"""
This module defines a function that returns a list of tuples,
each containing an element and its length.
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of a list of sequences.
    """
    return [(i, len(i)) for i in lst]
