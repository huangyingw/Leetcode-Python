class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        result = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                pre = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i])
                    result += (h - height[pre])*(i-1-stack[-1])
            stack.append(i)
        return result


class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if not height or len(height) <= 2: return 0
        result, i = 0, 0
        stack = []
        while i < len(height):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                pre = stack.pop()
                if stack:
                    h_min = min(height[stack[-1]], height[i])
                    result += (h_min - height[pre]) * (i - stack[-1] - 1)
        return result

