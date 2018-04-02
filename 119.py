class Solution:
    # def getRow(self, rowIndex):
    #     """
    #     :type rowIndex: int
    #     :rtype: List[int]
    #     """
    #     if rowIndex == 0: return [1]
    #     result = [1, 1]
    #     for i in range(2, rowIndex+1):
    #         prev = result
    #         result = [1] + [prev[j-1]+prev[j] for j in range(1, len(prev))] + [1]
    #     return result

    def getRow(self, rowIndex):
        result = [1]
        for _ in range(rowIndex):
            result = [x + y for x, y in zip([0] + result, result + [0])]
        return result