class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Space: O(m*n)
        # dp = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]

        # Space: O(min(m, n))
        if m > n: return self.uniquePaths(n, m)
        curr = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                curr[i] += curr[i - 1]
        return curr[m - 1]