#!/usr/bin/env python3

"""
    Returns the sum of a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    :param mxd_lst: The list of integers and floats.
    :return: The sum of the integers and floats in the list as a float.
    """
    return sum(mxd_lst)
