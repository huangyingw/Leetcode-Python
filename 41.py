# 可以换如果 target <= len(nums)
# 不可以换的时候找出nums[i] != i + 1, i+1就是最小的missing positive


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 1
        for i in range(len(nums)):
            target = nums[i]
            while target > 0 and target <= len(nums) and nums[target-1] != target:
                nums[target-1], target = target, nums[target-1]
        for i in range(0, len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        
# class Solution:
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         if not nums or len(nums) == 0:
#             return 1
#         ret = 1
#         nums = set(nums)
#         while True:
#             if ret in nums:
#                 ret += 1
#             else:
#                 return ret