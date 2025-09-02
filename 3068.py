class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        dp = [0, -10**18]
        for n in nums:
            c0, c1, x = dp[0] + n, dp[1] + n, n ^ k
            dp = [max(c0, dp[1] + x), max(c1, dp[0] + x)]
        return dp[0]