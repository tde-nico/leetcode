class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def can_eat_all(k):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
                if hours > h:
                    return False
            return True
        while l < r:
            m = (l + r) // 2
            if can_eat_all(m):
                r = m
            else:
                l = m + 1
        return l
        