'''
Time: O(mn)
Space: O(m or n)
'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        curr = [0]*(m+1)
        prev = [0]*(m+1)
        for i in range(1, m+1):
            prev[i] = prev[i-1] + 1
        for j in range(1, n+1):
            curr[0] = j
            for i in range(1, m+1):
                temp = prev[i-1] if word1[i-1] == word2[j-1] else prev[i-1]+1
                curr[i] = min(curr[i-1]+1, prev[i]+1, temp)
            prev, curr = curr, prev
        return prev[m]