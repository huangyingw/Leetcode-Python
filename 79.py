# time O(m*n*len(word))
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, x, y):
        if not word: return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[0]:
            return False
        tmp = board[x][y]
        board[x][y] = '#'
        neighbor = self.dfs(board, word[1:], x + 1, y) or self.dfs(board, word[1:], x - 1, y) \
                   or self.dfs(board, word[1:], x, y + 1) or self.dfs(board, word[1:], x, y - 1)
        board[x][y] = tmp
        return neighbor