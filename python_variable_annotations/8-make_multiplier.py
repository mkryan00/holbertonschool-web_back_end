#!/usr/bin/env python3
"""Task 8 - Module for creating a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier."""

    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
