class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        f = [0] * 3
        f[0], f[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + nums[i])
        return f[(len(nums) - 1) % 3]