#!/usr/bin/env python3
"""A class that implements the MRU caching algorithm"""

from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """Defines a MRU cache class"""

    def __init__(self):
        """initializes instance of cache"""
        self.order_list = deque([])
        super().__init__()

    def put(self, key, item):
        """Inserts an item into cache with given key

        If key or item is None, it does nothing.
        If the number of items in self.cache_data is higher
          than <BaseCaching.MAX_ITEMS>:
          (1). discards the first item put in cache (MRU algorithm)
          (2). prints DISCARD: with the <key> discarded, followed
               by a new line
        """
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and \
               key not in self.cache_data:
                old_key = self.order_list.pop()
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")
                self.order_list.append(key)
            else:
                if key in self.cache_data:
                    self.order_list.remove(key)
                self.order_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Fetches a value from the cache with its key
        Returns:
           value in cache with key <key> if <key> exists
           None if the key doesn’t exist in self.cache_data or
              is None
        """
        if key and key in self.cache_data:
            self.update_order_list(key)
            return self.cache_data.get(key)
        return None

    def update_order_list(self, key):
        """updates position of key in order_list
        Params:
          key(hashable): the recently accessed key
        Returns:
          None
        """
        self.order_list.remove(key)
        self.order_list.append(key)
