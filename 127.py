import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        front, back = set([beginWord]), set([endWord])
        wordList.discard(beginWord)
        result = 2
        while front:
            new_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        new_front.add(new_word)
            front = new_front & wordList
            if front & back:
                return result
            result += 1
            if len(front) > len(back):
                front, back = back, front
            wordList -= front
        return 0