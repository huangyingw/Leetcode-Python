# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf4_pointer = 0
        self.buf4_count = 0
        self.buf4 = [''] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.buf4_pointer == 0:
                self.buf4_count = read4(self.buf4)
            if self.buf4_count == 0:
                break
            while i < n and self.buf4_pointer < self.buf4_count:
                buf[i] = self.buf4[self.buf4_pointer]
                self.buf4_pointer += 1
                i += 1
            if self.buf4_pointer >= self.buf4_count:
                self.buf4_pointer = 0
        return i