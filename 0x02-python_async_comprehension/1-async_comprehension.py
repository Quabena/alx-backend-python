#!/usr/bin/env python3
"""
A module that demonstrate async comprehension with async_generator.
"""

from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Corountine that collects 10 random numbers from async_generator.

    It uses async comprehension to gather 10 random numbers.
    """

    return [num async for num in async_generator()]
