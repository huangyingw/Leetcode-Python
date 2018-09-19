class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            return 0 if int(x[:0:-1]) > 2147483648 else -int(x[:0:-1])
        else:
            return 0 if int(x[::-1]) > 2147483647 else int(x[::-1])


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        while x != 0:
            x, p = divmod(x, 10)
            if not neg and ((result > 2147483647 // 10) or (result == 2147483647 // 10 and p > 7)):
                return 0
            if neg and (result > 2147483648 // 10 or (result == 2147483648 // 10 and p > 8)):
                return 0
            result = result * 10 + p
        return -result if neg else result