class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        stack = []
        diff = -1

        for i, num in enumerate(nums):
            if not stack or num < stack[-1][0]:
                stack.append((num, i))

            if stack and stack[-1][1] < i and num > stack[-1][0]:
                diff = max(diff, num - stack[-1][0])

        return diff