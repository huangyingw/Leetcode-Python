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


# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         wordList = set(wordList)
#         if endWord not in wordList:
#             return 0
#         queue = set([beginWord])
#         wordList.discard(beginWord)
#         result = 1
#         while queue:
#             new_queue = set()
#             for word in queue:
#                 for i in range(len(word)):
#                     for c in string.ascii_lowercase:
#                         new_word = word[:i] + c + word[i+1:]
#                         if new_word == endWord:
#                             return result+1
#                         else:
#                             if new_word in wordList:
#                                 new_queue.add(new_word)
#             result += 1
#             queue = new_queue
#             wordList -= new_queue
#         return 0