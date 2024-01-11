#!/usr/bin/env python3
"""
    Returns a function that multiplies a float by the specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    :param multiplier: The float multiplier.
    :return: A function that takes a float and returns the product.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
