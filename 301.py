# O(nm) where m is the total "number of recursive calls" or "nodes in the search tree".
# Then you need to relate m to n in the worst case


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return [""]
        result = []
        self.remove(s, 0, 0, result, '(', ')')
        return result

    def remove(self, s, last_i, last_j, result, openP, closeP):
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == openP: count += 1
            if s[i] == closeP: count -= 1
            if count >= 0: continue
            for j in range(last_j, i + 1):
                if s[j] == closeP and (j == last_j or s[j - 1] != closeP):
                    self.remove(s[:j] + s[j + 1:], i, j, result, openP, closeP)
            return
        rs = s[::-1]
        if openP == '(':
            self.remove(rs, 0, 0, result, ')', '(')
        else:
            result.append(rs)