class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        root = [i for i in range(n)]
        result = n
        for edge in edges:
            left = self.findRoot(root, edge[0])
            right = self.findRoot(root, edge[1])

            if left != right:
                root[left] = right
                result -= 1
        return result

    def findRoot(self, root, node):
        while node != root[node]:
            root[node] = root[root[node]]
            node = root[root[node]]
        return node