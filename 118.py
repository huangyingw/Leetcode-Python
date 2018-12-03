from operator import add
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            ll = map(add, res[-1]+[0], [0]+res[-1])
            res.append(list(ll))
        return res if numRows else []