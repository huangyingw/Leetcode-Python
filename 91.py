class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        if 0 < int(s[0]) <=26:
            dp[1] = 1
        else:
            dp[1] = 0
        for i in range(1, n):
            if 0 < int(s[i]) <= 26:
                dp[i+1] += dp[i]
            if 0 < int(s[i-1:i+1]) <= 26 and s[i-1:i+1][0] != '0':
                dp[i+1] += dp[i-1]
        return dp[n]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        f0 = 0
        e0, e1, e2 = 1, 0, 0
        for c in s:
            f0 = (c > '0') * e0 + e1 + e2 * (c < '7')
            e1 = e0 if c == '1' else 0
            e2 = e0 if c == '2' else 0
            e0 = f0
        return f0