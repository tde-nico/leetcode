class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum, minSum = 0, 0
        for n in nums:
            maxSum = max(0, maxSum+n)
            minSum = min(0, minSum+n)
        return maxSum - minSum