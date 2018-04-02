# time: log(n)
# space: log(n)

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            if n == -2147683648:
                n += 1
            n = -n
            x = 1/x
        return self.myPow(x*x, n/2) if n % 2 == 0 else x*self.myPow(x*x, int(n/2))