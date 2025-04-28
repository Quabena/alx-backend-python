#!/usr/bin/env python3
"""
Module that defines an asynchronous routine to run multiple
wait_random concurrently.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and
    return list of delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random.

    Returns:
        List[float]: List of all delays in ascending order of
        completion
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]

    for completed_task in asyncio.as_completed(tasks):
        delay: float = await completed_task
        delays.append(delay)

    return delays
