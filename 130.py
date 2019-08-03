class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(n):
            if board[0][i] == 'O': self.dfs(0, i, board)
            if board[m - 1][i] == 'O': self.dfs(m - 1, i, board)
        for i in range(1, m - 1):
            if board[i][0] == 'O': self.dfs(i, 0, board)
            if board[i][n - 1] == 'O': self.dfs(i, n - 1, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    board[i][j] = 'O'

    def dfs(self, x, y, board):
        board[x][y] = '1'
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                self.dfs(i, j, board)