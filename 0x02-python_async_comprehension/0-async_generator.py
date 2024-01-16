#!/usr/bin/env python3
"""
This module defines an asynchronous generator coroutine.

It loops 10 times, asynchronously waiting for 1 second each time,
and yields a random number between 0 and 10 using the random module.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Asynchronous generator coroutine.

    Yields a random number between 0 and 10 after waiting for 1 second.
    This process is repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
