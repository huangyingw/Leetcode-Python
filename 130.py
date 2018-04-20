class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        # check borders first
        for i in range(m):
            self.check(i, 0, board, m, n)
            if n > 0:
                self.check(i, n - 1, board, m, n)
        for j in range(n):
            self.check(0, j, board, m, n)
            if m > 0:
                self.check(m - 1, j, board, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    board[i][j] = 'O'

    def check(self, i, j, board, m, n):
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = '1'
            self.check(i - 1, j, board, m, n)
            self.check(i + 1, j, board, m, n)
            self.check(i, j - 1, board, m, n)
            self.check(i, j + 1, board, m, n)