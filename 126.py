import string
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList: return []
        result = []
        tree = defaultdict(set)
        queue = {beginWord}
        wordList -= queue
        found = False

        while queue:
            newQueue = set()
            for word in queue:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord == endWord:
                            found = True
                        if newWord in wordList:
                            tree[word].add(newWord)
                            newQueue.add(newWord)
            if found: break
            queue = newQueue
            wordList -= queue
        result = []
        self.backtrack(beginWord, endWord, tree, [beginWord], result)
        return result

    def backtrack(self, beginWord, endWord, tree, path, result):
        if beginWord == endWord:
            result.append(path)
        for w in tree[beginWord]:
            self.backtrack(w, endWord, tree, path + [w], result)