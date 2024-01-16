#!/usr/bin/env python3
"""
Async Comprehension Module

This module defines an asynchronous comprehension function.

The asynchronous generator is imported dynamically
from the '0-async_generator' module.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    Asynchronous Comprehension Function

    Returns:
    - List[int]: A list of integers obtained asynchronously
                 from the async generator.
    """
    return [number async for number in async_generator()]
