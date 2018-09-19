# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cols = defaultdict(list)
        start, end = 0, 0
        queue = deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            cols[col].append(node.val)
            if node.left:
                start = min(start, col-1)
                queue.append((node.left, col-1))
            if node.right:
                end = max(end, col+1)
                queue.append((node.right, col+1))
        ret = []
        for i in range(start, end+1):
            ret.append(cols[i])
        return ret