class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        result, start, count = 0, 0, 0
        d = {}
        for i, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            if d[c] == 1:
                count += 1
            while count > k:
                prev = s[start]
                d[prev] -= 1
                start += 1
                if d[prev] == 0:
                    count -= 1
            result = max(result, i - start + 1)
        return result