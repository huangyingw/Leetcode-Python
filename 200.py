# time and space complexity: O(mn)

class Solution:
    # updated union find
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF[find(x)] = find(y)

        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        locs = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == '1'}
        UF = {n * i + j: n * i + j for (i, j) in locs}
        for i, j in locs:
            for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if x < 0 or y < 0 or x >= m or y >= n or (x, y) not in locs:
                    continue
                union(n * i + j, n * x + y)
        return len({find(x) for x in UF})

    # dfs
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

    # union find
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        roots = [-1] * (n * m)
        positions = [[i, j] for i in range(m) for j in range(n) if grid[i][j] == '1']
        result = 0
        neighbors = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for p in positions:
            root = n * p[0] + p[1]
            roots[root] = root
            result += 1
            for nb in neighbors:
                x, y = p[0] + nb[0], p[1] + nb[1]
                nb_root = n * x + y
                if x < 0 or x >= m or y < 0 or y >= n or roots[nb_root] == -1:
                    continue
                nb_root = self.findRoot(roots, nb_root)
                if root != nb_root:
                    result -= 1
                    roots[root] = nb_root
                    root = nb_root
        return result

    def findRoot(self, roots, node):
        while node != roots[node]:
            roots[node] = roots[roots[node]]
            node = roots[roots[node]]
        return node