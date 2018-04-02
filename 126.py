from collections import defaultdict
import string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        def backtrack(path, word, result):
            path.append(word)
            if word == endWord:
                result.append(path[:])
            else:
                for next_word in graph[word]:
                    backtrack(path, next_word, result)
            path.pop()

        wordList = set(wordList)
        if endWord not in wordList:
            return []
        graph = defaultdict(list)
        this_level = set([endWord])
        wordList.discard(endWord)
        wordList.add(beginWord)
        found = False
        while this_level:
            next_level = set()
            for word in this_level:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordList:
                            graph[new_word].append(word)
                            if new_word == beginWord:
                                found = True
                            else:
                                next_level.add(new_word)
            if found:
                break
            wordList -= next_level
            this_level = next_level
        result = []
        backtrack([], beginWord, result)
        return result