class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        left = 0
        res = 0
        mpp = {}
        for i in range(len(nums)):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1
            while len(mpp) == k:
                res += len(nums) - i
                mpp[nums[left]] -= 1
                if mpp[nums[left]] == 0:
                    del mpp[nums[left]]
                left += 1
        return res