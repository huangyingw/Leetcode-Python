class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 2: return 0
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            res = max(res, (r-l)*h)
            while height[l] <= h and l < r:
                l += 1
            while height[r] <= h and l < r:
                r -= 1
        return res