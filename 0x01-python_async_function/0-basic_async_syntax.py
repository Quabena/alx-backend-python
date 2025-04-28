#!/usr/bin/env python3
"""
A module that defines an asynchronous coroutine to wait
for a random delay between 0 and 'max_delay' and
returns it.
"""


import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous wait for a random delay between 0 and max_delay seconds.

    Args: max_delay(int): The maximum delay value (default is 10).

    Returns:
        float: The random delay that was waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
