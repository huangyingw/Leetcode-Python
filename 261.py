class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        roots = [i for i in range(n)]
        count = n
        for edge in edges:
            left, right = self.findRoot(roots, edge[0]), self.findRoot(roots, edge[1])
            if left == right:
                return False
            roots[right] = left
            count -= 1
        return count == 1

    def findRoot(self, roots, node):
        while node != roots[node]:
            roots[node] = roots[roots[node]]
            node = roots[roots[node]]
        return node