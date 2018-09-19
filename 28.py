class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h, n = len(haystack), len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1