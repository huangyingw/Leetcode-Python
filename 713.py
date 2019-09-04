from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr, result, j = 1, 0, 0
        for i in range(len(nums)):
            curr *= nums[i]
            if curr >= k:
                while j <= i and curr >= k:
                    curr //= nums[j]
                    j += 1
            result += i - j + 1
        return result