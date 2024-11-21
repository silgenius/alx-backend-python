#!/usr/bin/env python3

"""contains a coroutine called async_generator
that takes no arguments.
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None, None]:
    """The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
