'''
Time: O(2^n)
Space: O(n)
'''

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        result = []
        self.dfs(n, n, '', result)
        return result

    def dfs(self, left, right, s, result):
        if right < left:
            return
        if not left and not right:
            result.append(s)
        if left:
            self.dfs(left - 1, right, s + '(', result)
        if right:
            self.dfs(left, right - 1, s + ')', result)