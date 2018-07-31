class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]: return []
        root = {}
        for word in words:
            curr = root
            for c in word:
                curr = curr.setdefault(c, {})
            curr['#'] = '#'
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]
        self.result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, '')
        return list(self.result)

    def dfs(self, board, x, y, trie, s):
        if '#' in trie:
            self.result.add(s)
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return
        if board[x][y] in trie and not self.visited[x][y]:
            self.visited[x][y] = True
            for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                xx, yy = x + i, y + j
                self.dfs(board, xx, yy, trie[board[x][y]], s + board[x][y])
            self.visited[x][y] = False