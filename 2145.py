class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        s, mx, mn = 0, 0, 0
        for x in differences:
            s += x
            mx = max(mx, s)
            mn = min(mn, s)
        return max(0, upper - lower - mx + mn + 1)