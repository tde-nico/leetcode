MOD = 10**9 + 7

class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1

        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) % MOD
            res = res * pow(i, -1, MOD) % MOD
        return res

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        formula = m * pow(m - 1, n - (k + 1), MOD)
        updated_formula = formula * self.nCr(n - 1, k) % MOD
        return updated_formula

        