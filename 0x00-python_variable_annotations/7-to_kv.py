#!/usr/bin/env python3
"""
    Returns a tuple with the string 'k' as the first element and
    the square of the int/float 'v' as the second element.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string 'k' as the first element and
    the square of the int/float 'v' as the second element.

    :param k: The string key.
    :param v: The int or float value.
    :return: A tuple (k, v**2).
    """
    return k, v ** 2.0
