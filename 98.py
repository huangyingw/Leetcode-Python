# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    #     if not root:
    #         return True
    #     if root.val <= floor or root.val >= ceiling:
    #         return False
    #     return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)

    
    def isValidBST(self, root):
        stack, prev, curr = [], None, root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            top = stack.pop()
            if prev and prev.val >= top.val:
                return False
            prev = top
            curr = top.right
        return True