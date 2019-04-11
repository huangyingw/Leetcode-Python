"""
Time: O(n logn)
Spac: O(26)
"""

from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        most_frequent = count.most_common(1)[0][1]
        add = 0
        for k, v in count.most_common()[1:]:
            if v == most_frequent:
                add += 1
        return max(len(tasks), (most_frequent - 1) * n + most_frequent + add)



