class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.findCombination(result, [], candidates, target)
        return result

    def findCombination(self, result, path, candidates, target):
        if target == 0:
            result.append(path.copy())
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            path.append(candidates[i])
            self.findCombination(result, path, candidates[i + 1:], target - candidates[i])
            path.pop()