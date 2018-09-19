class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i == 0:
            self.reverseSort(0, n - 1, nums)
            return
        else:
            j = n - 1
            while j >= i:
                if nums[j] > nums[i - 1]:
                    break
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            self.reverseSort(i, n - 1, nums)

    def reverseSort(self, start, end, nums):
        if start > end:
            return
        for i in range(start, (start + end) // 2 + 1):
            nums[i], nums[start + end - i] = nums[start + end - i], nums[i]