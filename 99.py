# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Space: O(1) with Morris Inorder traversal
class Solution:
    def __init__(self):
        self.previous = TreeNode(float('-inf'))
        self.first = None
        self.second = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, node):
        curr = node
        while curr:
            if not curr.left:
                self.findMistake(curr)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == curr:
                    prev.right = None  # restore the tree
                    self.findMistake(curr)
                    curr = curr.right
                else:
                    prev.right = curr
                    curr = curr.left

    def findMistake(self, node):
        if not self.first and self.previous.val >= node.val:
            self.first = self.previous
        if self.first and self.previous.val >= node.val:
            self.second = node
        self.previous = node