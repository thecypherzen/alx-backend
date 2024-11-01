#!/usr/bin/env python3
"""A caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Defines a Basic Cache"""

    def __init__(self):
        """initialises this cache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to cache
        If key or item is None, does nothing
        """
        if all([key, item]):
            self.cache_data[key] = item

    def get(self, key):
        """Returns value in cace at key
        If key is None or doesn't exist in dictionary, returns
        None
        """
        if key:
            return self.cache_data.get(key)
        return None
