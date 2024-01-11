#!/usr/bin/env python3
"""
    Returns the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    :param input_list: The list of floats.
    :return: The sum of the floats in the list.
    """
    return sum(input_list)
