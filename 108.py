# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# time: O(n)
# space O(logn)
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.dfs(0, len(nums) - 1, nums)

    def dfs(self, low, high, nums):
        if low > high: return None
        mid = low + (high - low) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(low, mid - 1, nums)
        root.right = self.dfs(mid + 1, high, nums)
        return root