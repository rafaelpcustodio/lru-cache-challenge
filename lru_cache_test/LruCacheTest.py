import unittest
from lru_cache.LruCache import LRUCache
from lru_generator.LruGeneratorCases import LruGeneratorCases

class LruCacheTest(unittest.TestCase):

    def test_period_smaller_than_expiration_value(self):
        expire_value = 120
        capacity = 2
        lru_test = LruGeneratorCases.create_lru(LruGeneratorCases(), capacity, expire_value)
        seconds = LruGeneratorCases.generate_case(LruGeneratorCases(), lru_test, 100000)
        self.assertGreaterEqual(expire_value, seconds)

    def test_period_bigger_than_expiration_value(self):
        expire_value = 1
        capacity = 2
        lru_test = LruGeneratorCases.create_lru(LruGeneratorCases(), capacity, expire_value)
        seconds = LruGeneratorCases.generate_case(LruGeneratorCases(), lru_test, 100000)
        self.assertGreaterEqual(expire_value, seconds)

if __name__ == '__main__':
    unittest.main()