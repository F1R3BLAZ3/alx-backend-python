#!/usr/bin/env python3
"""
Module for asynchronous coroutines using asyncio and random module.
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    with the specified max_delay.
    Returns a list of all the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
