#!/usr/bin/env python3
""" Writing strings to Redis  """
from typing import Union
import redis
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

