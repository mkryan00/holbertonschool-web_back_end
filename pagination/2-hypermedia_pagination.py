#!/usr/bin/env python3
"""Task 1 - Module to implement a method of pagination
    for baby names dataset.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the correct page of the dataset
        based on page and page_size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return dictionary with certain key-value pairs."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        page_size = len(data)

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next page": next_page,
            "prev page": prev_page,
            "total pages": total_pages
        }
