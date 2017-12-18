class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.length = len(nums)
        self.nums, self.bit = nums, [0] * (self.length + 1)
        for i in range(self.length):
            k = i + 1
            while k <= self.length:
                self.bit[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff, self.nums[i] = val - self.nums[i], val
        i += 1
        while i <= self.length:
            self.bit[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        result, j = 0, j + 1
        while j:
            result += self.bit[j]
            j -= (j & -j)
        while i:
            result -= self.bit[i]
            i -= (i & -i)
        return result


        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)
