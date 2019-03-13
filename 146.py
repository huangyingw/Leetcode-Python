class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
            self.dict[key] = n
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self.dict[key] = n
        self._add(n)
        if len(self.dict.keys()) > self.capacity:
            t = self.head.next
            self._remove(t)
            del self.dict[t.key]

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node



# from collections import OrderedDict
#
#
# class LRUCache(object):
#
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.cache:
#             return -1
#         result = self.cache[key]
#         del self.cache[key]
#         self.cache[key] = result
#         return result
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if key in self.cache:
#             del self.cache[key]
#         else:
#             if len(self.cache.keys()) == self.capacity:
#                 self.cache.popitem(last=False)
#         self.cache[key] = value