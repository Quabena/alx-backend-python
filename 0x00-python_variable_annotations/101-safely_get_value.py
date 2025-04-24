#!/usr/bin/env python3
"""
This module defines a function that safely retrieves a value from a mapping.
"""

from typing import Any, Mapping, TypeVar, Optional

T = TypeVar('T')
K = TypeVar('K')


def safely_get_value(
    dct: Mapping[K, T],
    key: K,
    default: Optional[T] = None
) -> Optional[T]:
    """
    Retrieves a value from a mapping if the key exists,
    otherwise returns default.

    Args:
        dct (Mapping[K, T]): A mapping of keys to values.
        key (K): The key to look for.
        default (Optional[T]): The value to return if the key is not found.

    Returns:
        Optional[T]: The value associated with the key or the default.
    """
    if key in dct:
        return dct[key]
    return default
