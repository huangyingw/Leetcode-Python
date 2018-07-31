class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m <= 0 or n <= 0: return []
        islands = [-1] * (n * m)
        neighbor = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        result, count = [], 0
        for p in positions:
            root = n * p[0] + p[1]
            islands[root] = root
            count += 1
            for nb in neighbor:
                x, y = p[0] + nb[0], p[1] + nb[1]
                n_idx = n * x + y
                if x < 0 or x >= m or y < 0 or y >= n or islands[n_idx] == -1:
                    continue

                root_n = self.findRoot(islands, n_idx)
                if root_n != root:
                    islands[root] = root_n
                    root = root_n
                    count -= 1
            result.append(count)
        return result

    def findRoot(self, islands, root):
        while root != islands[root]:
            islands[root] = islands[islands[root]]
            root = islands[islands[root]]
        return root