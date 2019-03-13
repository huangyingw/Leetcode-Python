# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


from collections import defaultdict


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = defaultdict(lambda: Node(0, None, None))
        d[None] = None
        n = head
        while n:
            d[n].val = n.val
            d[n].next = d[n.next]
            d[n].random = d[n.random]
            n = n.next
        return d[head]