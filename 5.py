"""
Time complexity: O(n^2)
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            # odd case
            palindrom1 = self.get_palindrom(i, i, s)
            if len(palindrom1) > len(result):
                result = palindrom1

            # even case
            palindrom2 = self.get_palindrom(i, i + 1, s)
            if len(palindrom2) > len(result):
                result = palindrom2
        return result

    def get_palindrom(self, right, left, s):
        while right >= 0 and left < len(s) and s[right] == s[left]:
            right -= 1
            left += 1
        return s[right + 1:left]