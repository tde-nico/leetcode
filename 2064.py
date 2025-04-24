class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(m: int) -> bool:
            s = sum((q + m - 1) // m for q in quantities)
            return s <= n
        l, r = 1, max(quantities)
        while l < r:
            mid = (l + r) // 2
            if canDistribute(mid):
                r = mid
            else:
                l = mid + 1
        return l
