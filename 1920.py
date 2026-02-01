class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ns = [0] * len(nums)
        for i in range(len(nums)):
            ns[i] = nums[nums[i]]
        return ns
        