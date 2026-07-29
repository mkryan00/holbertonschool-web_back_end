#!/usr/bin/env python3
"""Task 5 - Sums a list of floats as arguments and returns float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Compute the sum of a list of floats.
    """
    return float(sum(input_list))
