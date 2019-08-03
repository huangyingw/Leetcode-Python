class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0: return 0
        if n <= 1: return 1

        def find(x):
            while x != UF[x]:
                UF[x] = UF[UF[x]]
                x = UF[UF[x]]
            return x

        UF = [i for i in range(n)]
        result = n
        for x, y in edges:
            if UF[find(x)] != UF[find(y)]:
                result -= 1
                UF[find(x)] = UF[find(y)]
        return result