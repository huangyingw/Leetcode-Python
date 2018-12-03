class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        curr, num_of_chars = [], 0
        for w in words:
            if len(curr) + num_of_chars + len(w) > maxWidth:
                for i in range(maxWidth-num_of_chars):
                    curr[i%(len(curr)-1 or 1)] += ' '
                res.append(''.join(curr))
                curr = []
                num_of_chars = 0
            curr += [w]
            num_of_chars += len(w)
        return res + [' '.join(curr).ljust(maxWidth)]