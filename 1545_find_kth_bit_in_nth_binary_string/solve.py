class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        l = (1 << n) - 1
        mid = l // 2 + 1
        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)
        if self.findKthBit(n - 1, l - k + 1) == '0':
            return '1'
        return '0'
