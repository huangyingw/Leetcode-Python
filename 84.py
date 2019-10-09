from typing import List


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        heights.append(-1)
        result, i = 0, 0
        while i < len(heights):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                pre = stack.pop()
                result = max(result, heights[pre]*(i-1-stack[-1]))
        return result