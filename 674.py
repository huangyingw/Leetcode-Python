class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        curr = 1
        result = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
                result = max(curr, result)
            else:
                curr = 1
        return result