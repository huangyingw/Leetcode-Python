"""
Time complexity: O(n logn)
Space complexity: O(26)
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = [0] * 26
        for i in tasks:
            c[ord(i)-ord('A')] += 1
        c.sort()
        i = 25
        while i >= 0 and c[i] == c[25]:
            i -= 1
        return max(len(tasks), (c[25]-1)*(n+1)+25-i)