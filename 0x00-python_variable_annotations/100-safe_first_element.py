#!/usr/bin/env python3
"""
This module defines a duck-typed function that returns the first
element of a sequence if it exists, otherwise None.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists, else None.

    Args:
        lst (Sequence[Any]): A sequence of elements of unknown type.

    Returns:
        Optional[Any]: The first element if it exists, otherwise None.
    """

    if lst:
        return lst[0]
    else:
        return None
