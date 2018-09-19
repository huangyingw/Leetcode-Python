class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        sign = 1
        number = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    number = number*10 + int(s[i])
                    i += 1
                result += sign * number
            if i >= len(s):
                break
            if s[i] is '+':
                sign = 1
                number = 0
            if s[i] is '-':
                sign = -1
                number = 0
            if s[i] is '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            if s[i] is ')':
                result *= stack.pop()
                result += stack.pop()
                number = 0
                sign = 1
            i += 1
        return result