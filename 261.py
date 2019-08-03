class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = [i for i in range(n)]
        count = n
        for edge in edges:
            left, right = self.find(edge[0], UF), self.find(edge[1], UF)
            if left == right: return False
            count -= 1
            UF[right] = left
        return count == 1

    def find(self, node, UF):
        if UF[node] != node:
            UF[node] = self.find(UF[node], UF)
        return UF[node]


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