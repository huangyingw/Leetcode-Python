# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# time: O(nlog(n))

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for i in sorted(intervals, key=lambda x: x.start):
            if result and result[-1].end >= i.start:
                result[-1].end = max(i.end, result[-1].end)
                continue
            result.append(i)
        return result

