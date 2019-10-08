from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        roots = [i for i in range(n)]
        connect = n
        for edge in edges:
            left, right = self.find(edge[0], roots), self.find(edge[1], roots)
            if left == right: return False
            roots[right] = left
            connect -= 1
        return connect == 1

    def find(self, node, roots):
        root = node
        while root != roots[root]:
            root = roots[root]
        while node != root:
            node, roots[node] = roots[node], root
        return root


# class Solution:
#     def validTree(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: bool
#         """
#         roots = [i for i in range(n)]
#         count = n
#         for edge in edges:
#             left, right = self.findRoot(roots, edge[0]), self.findRoot(roots, edge[1])
#             if left == right:
#                 return False
#             roots[right] = left
#             count -= 1
#         return count == 1
#
#     def findRoot(self, roots, node):
#         while node != roots[node]:
#             roots[node] = roots[roots[node]]
#             node = roots[roots[node]]
#         return node