class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            while x != UF[x]:
                UF[x] = UF[UF[x]]
                x = UF[UF[x]]
            return x

        if len(positions) <= 1: return [len(positions)]
        UF = {}
        result, count = [], 0
        for i, j in positions:
            count += 1
            curr = n * i + j
            UF.setdefault(curr, curr)
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and n * x + y in UF:
                    nn = find(n * x + y)
                    if nn != UF[find(curr)]:
                        UF[find(curr)] = nn
                        count -= 1
            result.append(count)
        return result