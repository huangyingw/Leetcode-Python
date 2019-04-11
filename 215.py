import heapq

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = self.findPivot(0, len(nums) - 1, nums, k)
        return nums[pivot]

    def findPivot(self, left, right, nums, k):
        i, j, p = left, right, right
        while i < j:
            if nums[i] < nums[p]:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        nums[i], nums[p] = nums[p], nums[i]
        offset = i - left + 1
        if offset == k:
            return i
        elif offset < k:
            return self.findPivot(i + 1, right, nums, k - offset)
        else:
            return self.findPivot(left, i - 1, nums, k)

    # k+(n-k)*log(k) time
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     q = nums[:k]
    #     heapq.heapify(nums)
    #     for num in nums[k:]:
    #         if num > q[0]:
    #             heapq.heapreplace(q, num)
    #     return q[0]

    # O(nlogn)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums)[-k]
