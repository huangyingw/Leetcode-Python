'''
Time complexity: O(N*N!)
'''
from collections import defaultdict


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        used = defaultdict(lambda: False)
        self.dfs(nums, ret, [], used)
        return ret

    def dfs(self, nums, ret, permutation, used):
        if len(nums) == len(permutation):
            ret.append(permutation)
        for i in range(len(nums)):
            if used[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue
            used[i] = True
            self.dfs(nums, ret, permutation + [nums[i]], used)
            used[i] = False