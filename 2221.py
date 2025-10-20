class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)-1
        res = nums[0]
        pascal = 1
        for k in range(1, n+1):
            pascal = pascal * (n-k+1) // k
            res = (res + nums[k] * pascal) % 10
        return res