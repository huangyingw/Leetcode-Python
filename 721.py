from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owners, roots = {}, {}
        for account in accounts:
            for i in range(1, len(account)):
                roots[account[i]] = account[i]
                owners[account[i]] = account[0]

        for account in accounts:
            root = self.findRoot(account[1], roots)
            for i in range(1, len(account)):
                roots[self.findRoot(account[i], roots)] = root

        unions = defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                root = self.findRoot(account[i], roots)
                unions[root].add(account[i])

        result = []
        for k, v in unions.items():
            one_account = [owners[k]] + sorted(list(v))
            result.append(one_account)
        return result

    def findRoot(self, node, roots):
        while roots[node] != node:
            roots[node] = roots[roots[node]]
            node = roots[roots[node]]
        return node
