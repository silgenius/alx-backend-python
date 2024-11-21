#!/usr/bin/env python3

"""Contains async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension four
times in parallel using asyncio.gather"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time = time.perf_counter()
    await asyncio.gather(* (async_comprehension() for _ in range(10)))
    elasped_time = time.perf_counter() - start_time
    return elasped_time
