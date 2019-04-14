from lru_cache.LruCache import LRUCache
from datetime import datetime

class LruGeneratorCases(object):

    def create_lru(self, capacity, expires):
        return LRUCache(capacity, expires)

    def generate_case(self, lru, ranged):
        time_initialized = datetime.now().second
        for index in range(ranged):
            LRUCache.set(lru, 'test{0}'.format(index), index)
            print(lru.get('test{0}'.format(index)))
            if lru.get('test{0}'.format(index)) < 0:
                break
        time_finalized = datetime.now().second
        return time_finalized - time_initialized
