class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_index = {c:i for i, c in enumerate(S)}
        left = right = 0
        result = []
        for i in range(0, len(S)):
            right = max(right, last_index[S[i]])
            if i == right:
                result.append(right-left+1)
                left = i + 1
        return result