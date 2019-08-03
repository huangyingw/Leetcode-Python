class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, result, [])
        return result

    def dfs(self, candidates, target, result, path):
        if target < 0: return
        if target == 0: result.append(path)
        for i in range(len(candidates)):
            if candidates[i] > target: break
            self.dfs(candidates[i:], target - candidates[i], result, path + [candidates[i]])