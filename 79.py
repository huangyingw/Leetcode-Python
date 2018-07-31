class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word[1:], set([(i, j)])):
                        return True
        return False

    def dfs(self, board, x, y, word, visited):
        if word == '': return True
        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            xx, yy = x + i, y + j
            if 0 <= xx < len(board) and 0 <= yy < len(board[0]) and board[xx][yy] == word[0] and (
            xx, yy) not in visited:
                visited.add((xx, yy))
                if self.dfs(board, xx, yy, word[1:], visited):
                    return True
                visited.remove((xx, yy))
        return False