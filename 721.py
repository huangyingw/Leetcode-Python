class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        result = []
        roots, names = {}, {}
        for account in accounts:
            for i in account[1:]:
                names[i] = account[0]
                roots[i] = i
        # merge
        for account in accounts:
            r = self.find(account[1], roots)
            for i in account[2:]:
                roots[self.find(i, roots)] = r
        unions = defaultdict(set)
        for account in accounts:
            for i in account[1:]:
                unions[self.find(i, roots)].add(i)

        for k, v in unions.items():
            result.append([names[k]] + sorted(list(v)))
        return result

    def find(self, node, roots):
        root = node
        while root != roots[root]:
            root = roots[root]
        while node != root:
            node, roots[node] = roots[node], root
        return root