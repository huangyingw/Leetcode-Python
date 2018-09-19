class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def firstGreat(array, x):
            l, r = 0, len(array)-1
            while l <= r:
                m = l + (r - l) // 2
                if array[m] < x:
                    l = m + 1
                else:
                    r = m - 1
            return l
        if not nums: return [-1, -1]
        start = firstGreat(nums, target)
        end = firstGreat(nums, target+1) - 1
        if start <= end:
            return [start, end]
        return [-1, -1]
