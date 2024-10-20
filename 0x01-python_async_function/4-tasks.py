#!/usr/bin/env python3

"""
an async routine called wait_n that takes in 2 int arguments
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values)
    """
    tasks = [task_wait_random(max_delay) for task in range(n)]
    res = await asyncio.gather(*tasks)
    return sorted(res)
