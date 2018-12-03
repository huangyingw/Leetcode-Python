# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        self.dfs(root, sum, res, [])
        return res

    def dfs(self, root, sum, res, path):
        if not root: return
        if not root.left and not root.right and root.val == sum:
            path.append(root.val)
            res.append(path)
        self.dfs(root.left, sum - root.val, res, path + [root.val])
        self.dfs(root.right, sum - root.val, res, path + [root.val])