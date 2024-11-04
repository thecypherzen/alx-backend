#!/usr/bin/env python3
"""A class that implements the LFU caching algorithm"""

from base_caching import BaseCaching
from collections import deque


class LFUCache(BaseCaching):
    """Defines a LFU cache class"""

    def __init__(self):
        """initializes instance of cache"""
        self.order_list = deque([])
        self.counts = {}
        super().__init__()

    def get_min_vals(self):
        """gets the key with minimum frequency

        Returns
           index of key to be removed
        """
        count = 0   # number of items with matching freqs
        min_freq = self.counts.get(self.order_list[0])
        min_i, cur_i = (0, 0)
        while cur_i < self.MAX_ITEMS:
            freq = self.counts.get(self.order_list[cur_i])
            if freq < min_freq:
                min_freq = freq
                count, min_i = (1, cur_i)
            elif freq == min_freq:
                count += 1
            cur_i += 1
        return min_i

    def put(self, key, item):
        """Inserts an item into cache with given key

        If key or item is None, it does nothing.
        If the number of items in self.cache_data is higher
          than <BaseCaching.MAX_ITEMS>:
          (1). discards the first item put in cache (LFU algorithm).
               if multiple items are conflicting, the LRU is used as
               the tie breaker.
          (2). prints DISCARD: with the <key> discarded, followed
               by a new line
        """
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and \
               key not in self.cache_data:
                # get index of key to discard and discard
                index = self.get_min_vals()
                old_key = self.order_list[index]
                self.order_list.remove(old_key)
                del self.cache_data[old_key]
                del self.counts[old_key]
                print(f"DISCARD: {old_key}")
                self.order_list.append(key)
            else:
                # reposition matching key
                if key in self.cache_data:
                    self.order_list.remove(key)
                self.order_list.append(key)

            # globally update cache and keys counts
            self.cache_data[key] = item
            self.counts[key] = 0 if key not in self.counts \
                else self.counts[key] + 1


    def get(self, key):
        """Fetches a value from the cache with its key
        Returns:
           value in cache with key <key> if <key> exists
           None if the key doesn’t exist in self.cache_data or
              is None
        """
        if key and key in self.cache_data:
            self.order_list.remove(key)
            self.order_list.append(key)
            self.counts[key] += 1
            return self.cache_data.get(key)
        return None
