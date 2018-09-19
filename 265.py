class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]: return 0
        pmin1, pmin2 = -1, -1
        m, n = len(costs), len(costs[0])
        for i in range(m):
            min1, min2 = -1, -1
            for j in range(n):
                if pmin1 != j:
                    costs[i][j] += 0 if pmin1 < 0 else costs[i - 1][pmin1]
                else:
                    costs[i][j] += 0 if pmin2 < 0 else costs[i - 1][pmin2]

                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2, min1 = min1, j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
            pmin1, pmin2 = min1, min2

        return costs[m - 1][min1]