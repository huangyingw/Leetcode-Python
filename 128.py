from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = set(nums)
        roots = {num: num for num in nums}

        for num in nums:
            root = self.findRoot(num, roots)
            if num + 1 in nums:
                child = self.findRoot(num + 1, roots)
                roots[child] = root
            elif num - 1 in nums:
                child = self.findRoot(num - 1, roots)
                roots[child] = root
        unions = defaultdict(list)
        for k, v in roots.items():
            root = self.findRoot(k, roots)
            unions[root].append(k)
        result = sorted(unions.items(), key=lambda x: len(x[1]), reverse=True)[0]
        return len(result[1])

    def findRoot(self, node, roots):
        while roots[node] != node:
            roots[node] = roots[roots[node]]
            node = roots[roots[node]]
        return node