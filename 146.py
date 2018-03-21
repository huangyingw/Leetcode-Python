from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        result = self.cache[key]
        del self.cache[key]
        self.cache[key] = result
        return result

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            del self.cache[key]
        else:
            if len(self.cache.keys()) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value