#!/usr/bin/env python3
"""Task 0 - A function that takes two integer arguments
    returns a tuple of size two containing start and end indices.
"""


def index_range(page, page_size):
    """Calculate the start and end index fora. give page and page size.

    Returns a tuple containing the start index and end index.
    """

    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
