class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i >> j & 1:
                    tmp.append(nums[j])
            result.append(tmp)
        return result


#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
#         self.dfs(nums, 0, [], result)
#         return result

#     def dfs(self, nums, index, path, result):
#         result.append(path)
#         for i in range(index, len(nums)):
#             self.dfs(nums, i+1, path+[nums[i]], result)