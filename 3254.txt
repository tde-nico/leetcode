class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        i, w = 0, 0
        while i < n:
            if i > 0 and nums[i] - nums[i - 1] != 1:
                w = i
            while w < i and i - w + 1 > k:
                w += 1
            if i - w + 1 == k:
                ans[i - k + 1] = nums[i]
            i += 1
        return ans
