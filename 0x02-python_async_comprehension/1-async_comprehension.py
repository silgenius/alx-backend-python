#!/usr/bin/env python3

"""contains async_generator from the previous task and then a
coroutine called async_comprehension that takes no arguments.
"""

from typing import Generator
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """using an async comprehensing over async_generator"""
    return [n async for n in async_generator()]
