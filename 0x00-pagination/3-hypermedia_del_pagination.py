#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Enforces data integrity after deletes

        Params:
           index(int): the current start index of the return page.
             That is the index of the first item in the current page.
           next_incex(int): the next index to query with. That should
              be the index of the first item after the last item on
              the current page.
           page_size(int): the current page size
           data(obj:list[list[str]]): the actual page of the dataset

        Requirements/Behavior:
          (1). Use assert to verify that index is in a valid range.
          (2). If the user queries index 0, page_size 10, they will
               get rows indexed 0 to 9 included.
          (3). If they request the next index (10) with page_size 10,
               but rows 3, 6 and 7 were deleted, the user should still
               receive rows indexed 10 to 19 included.
        """
        assert isinstance(index, int) and index >= 0 \
            and index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0 \
            and page_size < len(self.__indexed_dataset)
        result = []
        next_idx = None
        current_idx = index
        items = 0
        while True:
            if items == page_size:
                break
            data = self.__indexed_dataset.get(current_idx)
            next_idx = current_idx + 1
            if data:
                result.append(data)
                items += 1
            current_idx = next_idx
        return {
            "index": index,
            "next_index": next_idx,
            "page_size": page_size,
            "data": result
        }
