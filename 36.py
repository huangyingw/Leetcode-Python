class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValidUnit(row):
                return False

        for col in zip(*board):
            if not self.isValidUnit(col):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValidUnit(square):
                    return False
        return True

    def isValidUnit(self, unit):
        vals = [i for i in unit if i != '.']
        return len(set(vals)) == len(vals)