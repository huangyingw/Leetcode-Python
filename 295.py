from heapq import *


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first, self.second = [], []

    def addNum(self, num: int) -> None:
        if len(self.first) == len(self.second):
            heappush(self.second, -heappushpop(self.first, -num))
        else:
            heappush(self.first, -heappushpop(self.second, num))

    def findMedian(self) -> float:
        if len(self.first) == len(self.second):
            return (-self.first[0] + self.second[0]) / 2
        else:
            return float(self.second[0])