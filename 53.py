class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        max_so_far = result = nums[0]
        for i in nums[1:]:
            max_so_far = max(i, max_so_far+i)
            result = max(result, max_so_far)
        return result