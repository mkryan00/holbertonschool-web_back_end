#!/usr/bin/env python3
"""Task 0 - Module that provides a helper function,
    for pagination index calculation.
"""


def index_range(page, page_size):
    """Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): the number of items per page.

    Returns:
        tuple: a tuple containing the start index and end index.
    """

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
