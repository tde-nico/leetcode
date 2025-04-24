class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        s, c = 0, 0
        for x in range(1, n+1):
            if x not in banned:
                s += x
                if s > maxSum: break
                c += 1
        return c