#!/usr/bin/env python3
"""
    Returns a list of tuples containing elements from the input list
    and their lengths.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements from the input list
    and their lengths.

    :param lst: An iterable of sequences.
    :return: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
