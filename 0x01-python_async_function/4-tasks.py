#!/usr/bin/env python3
"""
A module that defines an async function to run multiple
task_wait_random concurrently
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently and return list
    of delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay for each task

    Returns:
        List[float]: List of all delays, sorted in ascending order.
    """

    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
