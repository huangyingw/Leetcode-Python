'''
Time: O(2^n)
Space: O(n)
'''

class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        dp = [[] for _ in range(n+1)]
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]

    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     if n < 1:
    #         return []
    #     result = []
    #     self.dfs(n, n, '', result)
    #     return result
    #
    # def dfs(self, left, right, s, result):
    #     if right < left:
    #         return
    #     if not left and not right:
    #         result.append(s)
    #     if left:
    #         self.dfs(left - 1, right, s + '(', result)
    #     if right:
    #         self.dfs(left, right - 1, s + ')', result)