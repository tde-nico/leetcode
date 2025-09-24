class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            digits = int(math.log10(i)) + 1
            if digits % 2 == 0:
                count += 1
        return count