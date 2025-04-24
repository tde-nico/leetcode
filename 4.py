class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1
        n = n1 + n2
        mid = (n+1) // 2
        l, r = 0, n1
        while l <= r:
            m1 = (l + r) // 2
            m2 = mid - m1
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if m1 < n1: r1 = nums1[m1]
            if m2 < n2: r2 = nums2[m2]
            if m1-1 >= 0: l1 = nums1[m1-1]
            if m2-1 >= 0: l2 = nums2[m2-1]
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                r = m1 - 1
            else:
                l = m1 + 1
        return 0
        