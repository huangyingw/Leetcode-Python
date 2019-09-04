class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for i, j in zip(s, t):
            if (i in ds and ds[i] != j) or (j in dt and dt[j] != i):
                return False
            ds[i] = j
            dt[j] = i
        return True