# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        dummy = ListNode(0)
        while s1 or s2 or carry:
            carry += (s1.pop() if s1 else 0) + (s2.pop() if s2 else 0)
            carry, val = divmod(carry, 10)
            tail = ListNode(val)
            tail.next = dummy.next
            dummy.next = tail
        return dummy.next