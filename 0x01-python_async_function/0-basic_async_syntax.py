#!/usr/bin/env python3

"""
 an asynchronous coroutine that takes in an integer argument
 that waits for a random delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    that waits for a random delay between 0 and max_delay
    """

    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
