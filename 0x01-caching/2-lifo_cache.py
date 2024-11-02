#!/usr/bin/env python3
"""A LIFO class"""

from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """Defines a FIFO cache class"""

    def __init__(self):
        """initializes instance of cache"""
        self.queue = deque([])
        super().__init__()

    def put(self, key, item):
        """Inserts an item into cache with given key

        If key or item is None, it does nothing.
        If the number of items in self.cache_data is higher
          than <BaseCaching.MAX_ITEMS>:
          (1). discards the first item put in cache (LIFO algorithm)
          (2). prints DISCARD: with the <key> discarded, followed
               by a new line
        """
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and \
               key not in self.cache_data.keys():
                old_key = self.queue.pop()
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Fetches a value from the cache with its key
        Returns:
           value in cache with key <key> if <key> exists
           None if the key doesn’t exist in self.cache_data or
              is None
        """
        if key:
            return self.cache_data.get(key)
        return None
