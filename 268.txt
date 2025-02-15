class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        s = set(range(n+1))
        for num in nums:
            s.remove(num)
        return list(s)[0]
        