#!/usr/bin/env python3
"""
Exercise for Redis to write strings- 0
"""

import redis
from typing import Union

class Cache:
    """Cache class for storing and retrieving data in Redis."""

    def __init__(self):
        """Initialize the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()
        
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Store data in Redis with a random key.

            Args:
                data (Union[str, bytes, int, float]): The data to store.

            Returns:
                str: The key under which the data is stored.
            """
            
        key = self._redis.randomkey()
        key = f"data:{self._redis.incr('data_counter')}"
        self._redis.set(key, data)
        return key
