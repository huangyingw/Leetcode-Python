class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                ss = nums[i]+nums[l]+nums[r]
                if ss == target:
                    return ss
                if abs(ss-target) <= abs(ret-target):
                    ret = ss
                if ss > target:
                    r -= 1
                else:
                    l += 1
        return ret