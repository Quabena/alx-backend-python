#!/usr/bin/env python3
"""
A module that defines an asynchronous generator.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10

    It waits 1 second between each yield using asyncio.sleep.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
