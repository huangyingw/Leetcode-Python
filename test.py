class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

c = ListNode(2)
a = ListNode(1)
a.next = c
b = a
a.next = ListNode(3)
while b:
    print(b.val)
    b = b.next