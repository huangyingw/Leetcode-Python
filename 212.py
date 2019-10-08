class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, trie.root, result)
        return result

    def search(self, board, x, y, node, result):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        if board[x][y] not in node.children: return
        child = node.children[board[x][y]]
        if child.word:
            if child.word not in result:
                result.append(child.word)
        tmp = board[x][y]
        board[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if self.isValid(board, nx, ny):
                self.search(board, nx, ny, child, result)
        board[x][y] = tmp

    def isValid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != 0