class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if not height or len(height) <= 2: return 0
        start, end = 0, len(height)-1
        left, right = height[start], height[end]
        result = 0
        while start < end:
            if left <= right:
                result += max(left - height[start], 0)
                start += 1
                left = max(left, height[start])
            else:
                result += max(right - height[end], 0)
                end -= 1
                right = max(right, height[end])
        return result