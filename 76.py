from collections import defaultdict

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = float('inf')
        if not s: return ''
        count_t = defaultdict(lambda:0)
        for c in t:
            count_t[c] += 1
        len_t = len(t)
        start, end = 0, 0
        while end < len(s):
            if count_t[s[end]] > 0:
                len_t -= 1
            count_t[s[end]] -= 1
            end += 1
            while len_t == 0:
                if end - start < d:
                    d = end - start
                    head = start
                count_t[s[start]] += 1
                if count_t[s[start]] > 0:
                    len_t += 1
                start += 1
        return '' if d == float('inf') else s[head:head+d]