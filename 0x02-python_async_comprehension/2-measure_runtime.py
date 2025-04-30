#!/usr/bin/env python3
"""
A module to measure the runtime executing async_comprehension
four times in parallel
"""

import asyncio
import time
from typing import Any
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to measure the total runtime of executing asyn_comprehension
    four times in parallel using asyncio.gather

    Returns:
        The total runtime of the operation.
    """

    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    return end_time - start_time
