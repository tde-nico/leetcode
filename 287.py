class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[abs(nums[i])] *= -1
            if nums[abs(nums[i])] > 0:
                return abs(nums[i])
