# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Binary search of the tree
    def __init__(self):
        self.root = None

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not self.root: self.root = root
        if not root: return False
        if self.search(root, k - root.val): return True
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

    def search(self, node, k):
        curr = self.root
        while curr:
            if curr.val > k:
                curr = curr.left
            elif curr.val < k:
                curr = curr.right
            else:
                return True if curr != node else False
        return False


        # DFS recursion
        # def findTarget(self, root: TreeNode, k: int) -> bool:
        #     s = set()
        #     def solve(root, k, s):
        #         if not root: return False
        #         if k-root.val in s: return True
        #         s.add(root.val)
        #         return solve(root.left, k, s) or solve(root.right, k, s)
        #     return solve(root, k, s)

        # DFS iterative
        # def findTarget(self, root: TreeNode, k: int) -> bool:
        #     s = set()
        #     stack = [root]
        #     while stack:
        #         curr = stack.pop()
        #         if k-curr.val in s: return True
        #         s.add(curr.val)
        #         if curr.left: stack.append(curr.left)
        #         if curr.right: stack.append(curr.right)
        #     return False