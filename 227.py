class Solution:
    def calculate(self, s: str) -> int:
        def compute(b, a, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a // b

        def precede(curr, prev):
            if (curr == '*' or curr == '/') and (prev == '+' or prev == '-'):
                return False
            return True

        nums, ops = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                i -= 1
            if c in {'+', '-', '*', '/'}:
                while ops and precede(c, ops[-1]):
                    nums.append(compute(nums.pop(), nums.pop(), ops.pop()))
                ops.append(c)
            i += 1
        while ops:
            nums.append(compute(nums.pop(), nums.pop(), ops.pop()))
        return nums[0]