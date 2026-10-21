class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2 # easier to compute median later

        # l,r is a counter in first array, not pointer
        # so r can be equal to m
        l = 0
        r = m

        while l <= r:
            i = (l + r) // 2
            j = half - i

            left_nums1 = nums1[i - 1] if i > 0 else float("-inf")
            right_nums1 = nums1[i] if i < m else float("inf")
            left_nums2 = nums2[j - 1] if j > 0 else float("-inf")
            right_nums2 = nums2[j] if j < n else float("inf")

            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
                if (m + n) % 2 == 1:
                    return max(left_nums1, left_nums2)
                else:
                    return ((max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2)
            elif left_nums1 > right_nums2:
                r = i - 1
            else:
                l = i + 1



