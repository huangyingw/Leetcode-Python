# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        result = []
        this_level = [root]
        while this_level:
            result.append([node.val for node in this_level])
            this_level = [child for node in this_level for child in (node.left, node.right) if child]
        return result