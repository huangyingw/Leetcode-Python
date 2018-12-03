class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        curr = [1]*m
        if obstacleGrid[0][0] == 1:
            curr = [0]*m
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for r in range(i, m):
                    curr[r] = 0
                break
        for j in range(1, n):
            for i in range(m):
                if obstacleGrid[i][j] == 1:
                    curr[i] = 0
                else:
                    if i > 0:
                        curr[i] += curr[i-1]
        return curr[m-1]