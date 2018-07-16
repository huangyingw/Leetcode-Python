class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2 or k == 0:
            return 0
        l = len(prices)
        if 2 * l <= k:
            return self.quickSolve(prices)

        result = [[0] * (l + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            buy = float('-inf')
            for j in range(1, l + 1):
                buy, result[i][j] = max(buy, result[i - 1][j - 1] - prices[j - 1]), max(result[i][j - 1],
                                                                                        buy + prices[j - 1])
        return result[k][l]

    def quickSolve(self, prices):
        buy, sell = float('-inf'), 0
        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price)
        return sell