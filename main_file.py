from lru_cache.LruCache import LRUCache
import time

if __name__ == '__main__':
    lru_cache = LRUCache(2, 5)

    for index in range(100000000):
        LRUCache.set(lru_cache, 'test{0}'.format(index), index)
        print(lru_cache.get('test{0}'.format(index)))
