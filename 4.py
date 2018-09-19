class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        A, B = nums1, nums2
        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = imin + (imax - imin) // 2
            j = half - i
            if i < m and A[i] < B[j - 1]:
                # i is too small
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big
                imax = i - 1
            else:
                # found right i
                max_of_left = None
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                min_of_right = None
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2