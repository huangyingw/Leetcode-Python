# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(n)

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node):
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            self.result = max(self.result, left+right)
            return 1 + max(left, right)
        self.result = 0
        depth(root)
        return self.result