import heapq


class Solution:
    def trapRainWater(self, heightMap: 'List[List[int]]') -> 'int':
        if not heightMap or not heightMap[0]: return 0

        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if not visited[i][j]:
                        heapq.heappush(heap, (heightMap[i][j], i, j))
                        visited[i][j] = 1
        ret = 0
        while heap:
            min_height, i, j = heapq.heappop(heap)
            for (x, y) in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    ret += max(0, min_height - heightMap[x][y])

                    # this max() is very important
                    heapq.heappush(heap, (max(heightMap[x][y], min_height), x, y))
                    visited[x][y] = 1
        return ret