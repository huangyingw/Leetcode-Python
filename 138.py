# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


from collections import defaultdict


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = defaultdict(lambda: RandomListNode(0))
        d[None] = None
        n = head
        while n:
            d[n].label = n.label
            d[n].next = d[n.next]
            d[n].random = d[n.random]
            n = n.next
        return d[head]