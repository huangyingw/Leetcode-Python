# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 0: return -1
        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l