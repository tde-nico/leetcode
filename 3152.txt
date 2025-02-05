class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prev = nums[0] & 1
        parity = [0] * n
        j = 0
        for i in range(n):
            x = nums[i] & 1
            if x == prev:
                j += 1
            parity[i] = j
            prev = x
        m = len(queries)
        res = [False] * m
        for i, (s, t) in enumerate(queries):
            res[i] = (parity[s] == parity[t])
        return res
        