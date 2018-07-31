class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ## O(n)
        nums.sort()
        result = [[]]
        size = 0
        for i in range(len(nums)):
            start = size if i >= 1 and nums[i - 1] == nums[i] else 0
            size = len(result)
            temp = []
            for j in range(start, size):
                temp.append(result[j] + [nums[i]])
            result.extend(temp)
        return result