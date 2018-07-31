class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        t = self.trie
        for c in word:
            t = t.setdefault(c, {})
        t[None] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.trie)

    def dfs(self, word, trie):
        if word == '':
            return None in trie
        c = word[0]
        if c != '.':
            return c in trie and self.dfs(word[1:], trie[c])
        return any(self.dfs(word[1:], kid) for kid in trie.values() if kid)





        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)