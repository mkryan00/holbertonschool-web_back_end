#!/usr/bin/env python3
"""Task 6 - Complex types.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums integers and floats of a list.
    """
    return float(sum(mxd_lst))
