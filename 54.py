class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0: return []
        ret = []
        rowMin, rowMax, colMin, colMax = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while rowMin <= rowMax and colMin <= colMax:
            for j in range(colMin, colMax + 1):
                ret.append(matrix[rowMin][j])
            rowMin += 1

            for i in range(rowMin, rowMax + 1):
                ret.append(matrix[i][colMax])
            colMax -= 1

            if rowMin > rowMax or colMax < colMin:
                break

            for j in range(colMax, colMin - 1, -1):
                ret.append(matrix[rowMax][j])
            rowMax -= 1

            for i in range(rowMax, rowMin - 1, -1):
                ret.append(matrix[i][colMin])
            colMin += 1

        return ret