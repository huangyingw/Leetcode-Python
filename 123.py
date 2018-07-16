class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1, sell1 = float('-inf'), 0
        buy2, sell2 = float('-inf'), 0
        for price in prices:
            buy2, sell2 = max(buy2, sell1-price), max(sell2, buy2+price)
            buy1, sell1 = max(buy1, -price), max(sell1, buy1+price)
        return sell2