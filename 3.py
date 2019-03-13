class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, start, result = {}, 0, 0
        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            d[c] = i
            result = max(result, i - start + 1)
        return result