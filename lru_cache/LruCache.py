import collections
from datetime import datetime, timedelta

class LRUCache(object):


    def __init__(self, capacity, expires):
        self.expires = expires
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.time = datetime.now()

    def get_expire(self):
        return self.expires

    def get_time_created(self):
        return self.time

    def get(self, key):
        try:
            while datetime.now().second < self.time.second + self.expires:
                value = self.cache.pop(key)
                self.cache[key] = value
                return value
            self.cache.clear()
            print('expiration time cache was achieved. It will be cleared.')
            return -1
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            while datetime.now().second < self.time.second + self.expires:
                self.cache.pop(key)
            self.cache.clear()
            print('expiration time cache was achieved. It will be cleared.')
            return -1
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value