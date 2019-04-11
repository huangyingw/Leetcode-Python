class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        starts, ret, curr = {0:1}, 0, 0
        for num in nums:
            curr += num
            ret += starts.get(curr-k, 0)
            starts[curr] = starts.get(curr, 0) + 1
        return ret