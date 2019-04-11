import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        wordList.discard(beginWord)
        queue = {beginWord}
        result = 1
        while queue:
            new_queue = set()
            for word in queue:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word == endWord:
                            return result+1
                        elif new_word in wordList:
                            new_queue.add(new_word)
            result += 1
            queue = new_queue
            wordList -= queue
        return 0


        # wordList = set(wordList)
        # if endWord not in wordList: return 0
        # front, back = {beginWord}, {endWord}
        # wordList.discard(beginWord)
        # result = 1
        # while front:
        #     new_front = set()
        #     for word in front:
        #         for i in range(len(word)):
        #             for c in string.ascii_lowercase:
        #                 new_word = word[:i] + c + word[i+1:]
        #                 if new_word in wordList:
        #                     new_front.add(new_word)
        #     front = new_front
        #     result += 1
        #     if front & back: return result
        #     if len(front) > len(back):
        #         front, back = back, front
        #     wordList -= front    
        # return 0 