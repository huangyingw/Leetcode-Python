class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        product = 1
        for i in nums:
            output.append(product)
            product *= i
        product = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= product
            product *= nums[i]
        return output