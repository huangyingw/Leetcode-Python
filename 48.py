class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix[0]) < 1:
            return
        visited = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if not visited or (i, j) not in visited:
                    matrix[i][j], matrix[j][n-i-1] = matrix[j][n-i-1], matrix[i][j]
                    visited.append((i, j))
                    visited.append((j, n-i-1))