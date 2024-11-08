from math import isqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = -1
        m = {}
        nums.sort()
        for n in nums:
            sqrt = isqrt(n)
            if sqrt * sqrt == n and sqrt in m:
                m[n] = m[sqrt] + 1
                res = max(res, m[n])
            else:
                m[n] = 1
        return res
