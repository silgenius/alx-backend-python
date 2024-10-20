#!/usr/bin/env python3

"""
 a measure_time function with integers n and max_delay as arguments
 and measures the total execution time for wait_n(n, max_delay)
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elasped_time = time.perf_counter() - s
    return elasped_time / n
