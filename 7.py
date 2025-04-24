class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        m = 0
        if x < 0:
            x = -x
            m = 1
        
        while x:
            res += (x % 10)
            x //= 10
            if x:
                res *= 10

        if res > 2147483647 or res < -2147483648:
            return 0
        return -res if m else res
        