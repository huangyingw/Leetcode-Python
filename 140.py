class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, record):
        if s in record:
            return record[s]
        result = []
        if not s:
            result.append('')
            return result
        for word in wordDict:
            if s.startswith(word):
                for ss in self.dfs(s[len(word):], wordDict, record):
                    if ss:
                        result.append(word + ' ' + ss)
                    else:
                        result.append(word)
        record[s] = result
        return result