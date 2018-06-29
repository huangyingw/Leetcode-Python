class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return -1
        n = len(nums)
        p = self.pivot(nums, 0, n - 1, k)
        return nums[p]

    def pivot(self, nums, left, right, k):
        i, j, p = left, right, right
        while i < j:
            if nums[i] < nums[p]:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        nums[i], nums[p] = nums[p], nums[i]
        m = i - left + 1
        if m == k:
            return i
        elif m > k:
            return self.pivot(nums, left, i - 1, k)
        elif m < k:
            return self.pivot(nums, i + 1, right, k - m)