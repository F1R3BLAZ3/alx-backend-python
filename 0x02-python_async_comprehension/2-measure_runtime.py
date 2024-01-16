#!/usr/bin/env python3
"""
Measure Runtime Module

This module defines a coroutine to measure the total runtime
of async_comprehension.
"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of async_comprehension
    executed four times in parallel.

    Returns:
    - float: Total runtime in seconds.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()

    return end_time - start_time
