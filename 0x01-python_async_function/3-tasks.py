#!/usr/bin/env python3
"""
A module that defines a regular function to create an asyncio.Task
for wait_random
"""


import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random with the
    given max_delay.

    Args:
        max_delay(int): The maximum delay in seconds for the
        wait_random coroutine.

    Returns:
        Asyncio.Task: An asyncio Task object schedules to
        run wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
