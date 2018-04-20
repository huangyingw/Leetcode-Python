from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        maps = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = deque([c for c in maps[int(digits[0])]])
        for i in range(1, len(digits)):
            while result and len(result[0]) == i:
                item = result.popleft()
                result.extend([item + c for c in maps[int(digits[i])]])
        return list(result)