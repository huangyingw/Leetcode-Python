# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.result

    def helper(self, node):
        if not node: return [0, 0]
        increase, decrease = 1, 1
        if node.left:
            l = self.helper(node.left)
            if node.left.val == node.val + 1:
                increase = l[0] + 1
            elif node.left.val == node.val - 1:
                decrease = l[1] + 1
        if node.right:
            r = self.helper(node.right)
            if node.right.val == node.val + 1:
                increase = max(increase, r[0] + 1)
            if node.right.val == node.val - 1:
                decrease = max(decrease, r[1] + 1)
        self.result = max(self.result, increase + decrease - 1)
        return [increase, decrease]