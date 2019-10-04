class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        start, d = 0, {}
        c = result = 0
        for i, v in enumerate(s):
            if v not in d:
                c += 1
                while c > k:
                    d[s[start]] -= 1
                    if d[s[start]] == 0:
                        c -= 1
                        del d[s[start]]
                    start += 1
            d[v] = d.get(v, 0) + 1
            result = max(result, i - start + 1)
        return result
