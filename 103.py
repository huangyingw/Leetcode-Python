# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result, q, depth = [], deque(), 0
        q.append((root, depth))
        while q:
            curr, depth = q.popleft()
            if len(result) == depth:
                result.append([])
            if depth % 2 == 0:
                result[depth].append(curr.val)
            else:
                result[depth].insert(0, curr.val)
            depth += 1
            if curr.left:
                q.append((curr.left, depth))
            if curr.right:
                q.append((curr.right, depth))
        return result