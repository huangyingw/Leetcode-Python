class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) <= 2: return 0
        result = 0
        left_max, right_max = 0, 0
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                result += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                result += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return result