class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            if heights[i] < heights[stack[-1]]:
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i-stack[-1]-1
                    res = max(res, w*h)
            stack.append(i)
        heights.pop()
        return res