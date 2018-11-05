class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        ret = 0
        while left < right:
            h = min(height[left], height[right])
            ret = max(ret, h*(right-left))
            while height[left] <= h and left < right:
                left += 1
            while height[right] <= h and left < right:
                right -= 1
        return ret