'''
O(n^min(k, n-k))
'''

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        ll = list(range(1, n + 1))
        self.dfs(res, [], k, ll)
        return res

    def dfs(self, res, path, k, ll):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(ll)):
            self.dfs(res, path + [ll[i]], k, ll[i + 1:])