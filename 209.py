class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        ret, sum = float('inf'), 0
        while r < len(nums):
            sum += nums[r]
            r += 1
            while sum >= s:
                ret = min(ret, r - l)
                sum -= nums[l]
                l += 1
        return 0 if ret == float('inf') else ret