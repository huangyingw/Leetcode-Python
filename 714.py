class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        buy, sell = float('-inf'), 0
        for i in range(len(prices)):
            buy, sell = max(buy, sell-prices[i]), max(sell, buy+prices[i]-fee)
        return sell