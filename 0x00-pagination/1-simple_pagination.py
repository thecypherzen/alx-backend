#!/usr/bin/env python3
"""Defines a Server class and utility functions"""

import csv
import math
from typing import List, Mapping, Optional, Tuple


def index_range(*args, **kwargs) -> Tuple:
    """A function that takes two integer arguments

    Params:
    args(obj:tuple[int]): normally passed args,which are ints
    kwargs(obj:dict[str, int]): keyword arguments dictionary

    Returns:
        A tuple of size=2 containing a `start index` and an `end index`
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.

        Note:
           Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    if len(args) == 2:
        page, page_size = args
    elif len(kwargs) == 2:
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')
    else:
        return ()
    end = page * page_size
    return (end - page_size, end)


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes: Tuple = index_range(page=page, page_size=page_size)
        dataset = self.__dataset or self.dataset()
        return dataset[indexes[0]: indexes[1]]
