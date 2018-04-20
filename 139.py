class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        wordDict = set(wordDict)
        for j in range(1, len(s)+1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[len(s)]