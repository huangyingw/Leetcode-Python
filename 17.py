from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        match = {'0':'', '1': '', '2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = ['']
        for digit in digits:
            temp = [r+c for r in result for c in match[digit]]
            result = temp
        return result

        # if not digits: return []
        # maps = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # result = deque([c for c in maps[int(digits[0])]])
        # for i in range(1, len(digits)):
        #     while result and len(result[0]) == i:
        #         item = result.popleft()
        #         result.extend([item + c for c in maps[int(digits[i])]])
        # return list(result)