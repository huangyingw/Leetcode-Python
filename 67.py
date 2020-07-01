# class Solution:
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            carry, remainder = divmod(carry, 2)
            result = str(remainder) + result
            i -= 1
            j -= 1

        return result