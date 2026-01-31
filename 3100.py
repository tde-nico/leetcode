class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        n, k = numBottles, numExchange
        return int(n + ((-2*k + 3 + sqrt(4*k*k + 8*n - 12*k + 1)) // 2))
