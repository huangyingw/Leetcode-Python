# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        node = dummy = TreeLinkNode(0)
        while root:
            node.next = root.left
            if root.left:
                node = node.next
            node.next = root.right
            if root.right:
                node = node.next
            root = root.next
            if not root:
                node = dummy
                root = dummy.next