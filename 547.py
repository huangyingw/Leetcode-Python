class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(x):
            while x != UF[x]:
                UF[x] = UF[UF[x]]
                x = UF[UF[x]]
            return x

        N = len(M)
        result = N
        UF = [i for i in range(N)]
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1 and i != j:
                    if UF[find(i)] != find(j):
                        result -= 1
                        UF[find(i)] = find(j)
        return result