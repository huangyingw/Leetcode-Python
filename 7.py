class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        sign = 1
        if x[0] == '-':
            return 0 if int(x[:0:-1]) > 2147483648 else -int(x[:0:-1])
        else:
            return 0 if int(x[::-1]) > 2147483647 else int(x[::-1])
