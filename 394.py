class Solution:
    def decodeString(self, s: str) -> str:
        curr, count, stack = '', 0, []
        for c in s:
            if c == '[':
                stack.append(curr)
                stack.append(count)
                curr = ''
                count = 0
            elif c == ']':
                num = stack.pop()
                prev = stack.pop()
                curr = prev + num*curr
            elif c.isdigit():
                count = count*10 + int(c)
            else:
                curr += c
        return curr