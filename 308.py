class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.nums = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
        print(self.tree)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m == 0 or self.n == 0: return
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m == 0 or self.n == 0: return 0
        return self.getRangeSum(row2 + 1, col2 + 1) + self.getRangeSum(row1, col1) - self.getRangeSum(row2 + 1,
                                                                                                      col1) - self.getRangeSum(
            row1, col2 + 1)

    def getRangeSum(self, row, col):
        result, i = 0, row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return result


        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # obj.update(row,col,val)
        # param_2 = obj.sumRegion(row1,col1,row2,col2)
