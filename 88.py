class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mi = m - 1
        ni = n - 1
        r = m + n - 1
        while ni >= 0:
            if mi >= 0 and nums1[mi] > nums2[ni]:
                nums1[r] = nums1[mi]
                mi -= 1
            else:
                nums1[r] = nums2[ni]
                ni -= 1
            r -= 1
        