class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or len(s) == 0 or len(words) == 0: return []
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        result = []
        # same length of word in words
        n, m = len(words), len(words[0])
        for i in range(min(m, len(s) - m*n + 1)):
            curr = {}
            j = i
            while i + m*n <= len(s):
                word = s[j:j+m]
                j += m
                if word not in d:
                    i = j
                    curr.clear()
                else:
                    if word in curr:
                        curr[word] += 1
                    else:
                        curr[word] = 1
                    while curr[word] > d[word]:
                        curr[s[i:i+m]] -= 1
                        i += m
                    if j - i == m*n:
                        result.append(i)
        return result