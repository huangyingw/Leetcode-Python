class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        product = 1
        for i in nums:
            result.append(product)
            product *= i
        product = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= product
            product *= nums[j]
        return result