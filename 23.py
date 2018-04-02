# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        q = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(q, (node.val, idx, node))
        while q:
            val, idx, node = heapq.heappop(q)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                heapq.heappush(q, (node.next.val, idx, node.next))
        return dummy.next