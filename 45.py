class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps, currentEnd, currentFarthest = 0, 0, 0
        for i in range(len(nums)-1):
            currentFarthest = max(i+nums[i], currentFarthest)
            if i == currentEnd:
                jumps += 1
                currentEnd = currentFarthest
            if currentEnd > len(nums)-1:
                break
        return jumps