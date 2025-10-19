class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = [0] * 101
        mx = 0
        res = 0
        for n in nums:
            c[n] += 1
            cnt = c[n]
            if cnt > mx:
                mx = cnt
                res = cnt
            elif cnt == mx:
                res += cnt
        return res