from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)
        for ticket in sorted(tickets, reverse=True):
            targets[ticket[0]].append(ticket[1])
        stack, result = ['JFK'], []
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            result.append(stack.pop())
        return result[::-1]