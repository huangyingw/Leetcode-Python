from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d, curr, result = {0: 1}, 0, 0
        for num in nums:
            curr += num
            result += d.get(curr-k, 0)
            d[curr] = d.get(curr, 0) + 1
        return result