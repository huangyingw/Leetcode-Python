class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            item = nums.pop(0)
            i += 1
            if item  == val:
                continue
            else:
                nums.append(item)
        return len(nums)