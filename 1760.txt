class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l+r) // 2
            c = sum((x - 1) // m for x in nums)
            if c <= maxOperations:
                r = m
            else:
                l = m + 1
        return r
