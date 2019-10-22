class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 2: return len(nums)
        result, increase = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increase += 1
            else:
                increase = 1
            result = max(result, increase)
        return result