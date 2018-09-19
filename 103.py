# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, OrderedDict

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = deque([(root, 0)])
        mapping = OrderedDict()
        while queue:
            node, depth = queue.popleft()
            if depth % 2 == 0:
                if depth in mapping:
                    mapping[depth].append(node.val)
                else:
                    q = deque([node.val])
                    mapping[depth] = q
            else:
                if depth in mapping:
                    mapping[depth].appendleft(node.val)
                else:
                    q = deque([node.val])
                    mapping[depth] = q
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        result = []
        for _, v in mapping.items():
            result.append(list(v))
        return result