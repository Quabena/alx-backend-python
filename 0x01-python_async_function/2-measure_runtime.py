#!/usr/bin/env python3
"""
A module that defines a function to measure the average runtime
of wait_n.
"""


import asyncio
import time
from typing import Callable


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n(n, max_delay)

    Args:
        n(int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random.

    Returns:
        float: The average execution time per wait_random call.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
