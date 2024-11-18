class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() 
        def count(target):
            c = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= target:
                    c += (right - left)
                    left += 1
                else:
                    right -= 1
            return c
        up = count(upper)
        down = count(lower - 1)
        return up - down
