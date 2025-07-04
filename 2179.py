class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        mpp = {}
        for i, v in enumerate(nums1):
            mpp[v] = i
        n = len(nums2)
        total = 0
        st = []
        for x in nums2:
            idx = mpp[x]
            left = bisect.bisect_left(st, idx)
            right = (n - 1 - idx) - (len(st) - left)
            total += left * right
            bisect.insort(st, idx)
        return total
