class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        current, prev = nums[0], 0
        for i in nums[1:]:
            prev, current = current, max(prev+i, current)
        return current