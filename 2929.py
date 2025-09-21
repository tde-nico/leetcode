class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = (n + 2) * (n + 1) // 2
        for i in range(1, 4):
            rem = n - i * (limit + 1)
            if rem < 0:
                break
            val = (rem + 2) * (rem + 1) // 2
            c = 3 if i < 3 else 1
            res += -c * val if i % 2 else c * val
        return res