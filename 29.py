class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor, result = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            temp = 0
            while dividend >= divisor << (temp + 1): temp += 1
            result += 1 << temp
            dividend -= divisor << temp
        return min(result if sign else -result, INT_MAX)