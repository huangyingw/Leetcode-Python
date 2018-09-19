class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                s1, s2 = s[l:r], s[l+1:r+1]
                return s1[::-1] == s1 or s2[::-1] == s2
            l += 1
            r -= 1
        return True