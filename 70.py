class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        ret = [0]*n
        ret[0], ret[1] = 1, 2
        for i in range(2, n):
            ret[i] = ret[i-1] + ret[i-2]
        return ret[-1]